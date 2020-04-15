import pyrealsense2 as rs
import numpy as np
from object_detection.utils import ops as utils_ops
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util
import cv2
from matplotlib import pyplot as plt

points = rs.points()
pipeline= rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)
config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 30)
profile = pipeline.start(config)
depth_sensor = profile.get_device().first_depth_sensor()
depth_scale = depth_sensor.get_depth_scale()
align_to = rs.stream.color
align = rs.align(align_to)


from object_detection.object_detection_api import object_detection_api
detector = object_detection_api('exported_graphs')

import time
while True:
    frames = pipeline.wait_for_frames()
    aligned_frames = align.process(frames)
    aligned_depth_frame = aligned_frames.get_depth_frame()
    color_frame = aligned_frames.get_color_frame()
    im = np.asanyarray(color_frame.get_data())[400:,300:900,:]
    image_np = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    t0 = time.time()
    output_dict, category_index = detector.run(image_np)
    dt = time.time() - t0
    print("Time cost: %s"%dt)
    vis_util.visualize_boxes_and_labels_on_image_array(
        image_np,
        np.array([output_dict['detection_boxes'][0]]),
        np.array([output_dict['detection_classes'][0]]),
        np.array([output_dict['detection_scores'][0]]),
        category_index,
        instance_masks=output_dict.get('detection_masks'),
        use_normalized_coordinates=True,
        line_thickness=8)
    plt.figure(figsize=(12, 8))
    cv2.namedWindow("result", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("result", image_np[:,:,::-1])
    if cv2.waitKey(1) & 0xFF == ord('q'): break


cv2.destroyAllWindows()
