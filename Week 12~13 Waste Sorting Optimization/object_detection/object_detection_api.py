import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile

from distutils.version import StrictVersion
from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image

# This is needed since the notebook is stored in the object_detection folder.
sys.path.append("..")
from object_detection.utils import ops as utils_ops
from utils import label_map_util
from utils import visualization_utils as vis_util

# # Model preparation
# Any model exported using the `export_inference_graph.py` tool can be loaded here simply by changing `PATH_TO_FROZEN_GRAPH` to point to a new .pb file.
# By default we use an "SSD with Mobilenet" model here. See the [detection model zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md) for a list of other models that can be run out-of-the-box with varying speeds and accuracies.

def load_image_into_numpy_array(image):
  (im_width, im_height) = image.size
  return np.array(image.getdata()).reshape(
      (im_height, im_width, 3)).astype(np.uint8)

class object_detection_api(object):
    def __init__(self, model_name='ssd_mobilenet_v1_coco_2017_11_17'):
        # What model to download.
        self.model_name = model_name
        # MODEL_NAME = 'faster_rcnn_inception_resnet_v2_atrous_coco'
        # MODEL_NAME = 'faster_rcnn_resnet101_coco_2018_01_28'
        MODEL_FILE = self.model_name + '.tar.gz'
        DOWNLOAD_BASE = 'http://download.tensorflow.org/models/object_detection/'

        # Path to frozen detection graph. This is the actual model that is used for the object detection.
        PATH_TO_FROZEN_GRAPH = self.model_name + '/frozen_inference_graph.pb'

        # List of the strings that is used to add correct label for each box.
        self.PATH_TO_LABELS = os.path.join('data_trash', 'trash_label_map.pbtxt')

        # Download Model if not exits already
        if not os.path.exists(PATH_TO_FROZEN_GRAPH):
            opener = urllib.request.URLopener()
            opener.retrieve(DOWNLOAD_BASE + MODEL_FILE, MODEL_FILE)
            tar_file = tarfile.open(MODEL_FILE)
            for file in tar_file.getmembers():
              file_name = os.path.basename(file.name)
              if 'frozen_inference_graph.pb' in file_name:
                tar_file.extract(file, os.getcwd())

        # ## Load a (frozen) Tensorflow model into memory.
        self.detection_graph = tf.Graph()
        with self.detection_graph.as_default():
          od_graph_def = tf.GraphDef()
          with tf.gfile.GFile(PATH_TO_FROZEN_GRAPH, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

        with self.detection_graph.as_default():
          self.sess = tf.Session()
          # Get handles to input and output tensors
          ops = tf.get_default_graph().get_operations()
          all_tensor_names = {output.name for op in ops for output in op.outputs}
          self.tensor_dict = {}
          for key in [
              'num_detections', 'detection_boxes', 'detection_scores',
              'detection_classes', 'detection_masks']:
            tensor_name = key + ':0'
            if tensor_name in all_tensor_names:
              self.tensor_dict[key] = tf.get_default_graph().get_tensor_by_name(
                  tensor_name)

          self.image_tensor = tf.get_default_graph().get_tensor_by_name('image_tensor:0')

    def run_inference_for_single_image(self, image):

      # Run inference
      output_dict = self.sess.run(self.tensor_dict,
                             feed_dict={self.image_tensor: np.expand_dims(image, 0)})
      # all outputs are float32 numpy arrays, so convert types as appropriate
      output_dict['num_detections'] = int(output_dict['num_detections'][0])
      output_dict['detection_classes'] = output_dict[
          'detection_classes'][0].astype(np.uint8)
      output_dict['detection_boxes'] = output_dict['detection_boxes'][0]
      output_dict['detection_scores'] = output_dict['detection_scores'][0]
      if 'detection_masks' in output_dict:
        output_dict['detection_masks'] = output_dict['detection_masks'][0]
      return output_dict

    # the array based representation of the image will be used later in order to prepare the
    # result image with boxes and labels on it.
    def run(self, image_np):
        if len(image_np.shape)==3:
            # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
            image_np_expanded = np.expand_dims(image_np, axis=0)
        # Actual detection.
        output_dict = self.run_inference_for_single_image(image_np)
        # Label maps map indices to category names, so that when our convolution network predicts `5`, we know that this corresponds to `airplane`.  Here we use internal utility functions, but anything that returns a dictionary mapping integers to appropriate string labels would be fine
        category_index = label_map_util.create_category_index_from_labelmap(self.PATH_TO_LABELS, use_display_name=True)

        return output_dict, category_index

import cv2
if __name__ == '__main__':
    detector = object_detection_api()
    image = Image.open('test_images/image1.jpg')
    image_np = load_image_into_numpy_array(image)
    output_dict, category_index = detector.run(image_np)
    vis_util.visualize_boxes_and_labels_on_image_array(
      image_np,
      output_dict['detection_boxes'],
      output_dict['detection_classes'],
      output_dict['detection_scores'],
      category_index,
      instance_masks=output_dict.get('detection_masks'),
      use_normalized_coordinates=True,
      line_thickness=8)
    plt.figure(figsize=(12, 8))
    cv2.imwrite("hi.png",image_np[:,:,::-1])
    print('Finish detection image!')
