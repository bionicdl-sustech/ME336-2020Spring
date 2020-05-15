from rlbench import DomainRandomizationEnvironment
from rlbench import RandomizeEvery
from rlbench import VisualRandomizationConfig
from rlbench.action_modes import ActionMode, ArmActionMode
from rlbench.tasks import OpenDoor
import numpy as np

# We will borrow some from the tests dir
rand_config = VisualRandomizationConfig(
    image_directory='../tests/unit/assets/textures')

action_mode = ActionMode(ArmActionMode.ABS_JOINT_VELOCITY)
env = DomainRandomizationEnvironment(
    action_mode, randomize_every=RandomizeEvery.EPISODE,
    frequency=1, visual_randomization_config=None)
env.launch()
live_demos = True
task = env.get_task(OpenDoor)
demos = task.get_demos(2, live_demos=live_demos)

descriptions, obs = task.reset()
obs, reward, terminate = task.step(action)
print('Done')
env.shutdown()
