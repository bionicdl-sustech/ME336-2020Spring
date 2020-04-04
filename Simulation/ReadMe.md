# PyRep Simulation
We will do our project 1 Kinematic Picking in PyRep and project 2 Simulated Robot Player in simulation. The Simulation folder contains all the code and instructions to complete the two projects.

- [PyRep Simulation](#pyrep-simulation)
  - [File Structure](#file-structure)
  - [Project 1: Kinematic Picking in PyRep](#project-1-kinematic-picking-in-pyrep)
    - [Getting Started](#getting-started)
    - [Explanation of the main code](#explanation-of-the-main-code)
    - [TODO: your assignment](#todo-your-assignment)
  - [Project 2: Simulated Robot Player](#project-2-simulated-robot-player)

## File Structure

- [/scene](./scene): stores all the v-rep scene files ended with ".ttt"
- [/src](./src): backend python code put here
- [/tasks](./tasks):
  - [/BaseScene_test](./tasks/BaseScene_test): test scene file and backend code
  - [/Kine_picking](./tasks/Kine_picking): simulate kinematic picking

## Project 1: Kinematic Picking in PyRep
### Getting Started

Make sure you have followed the instructions below to install dependency: PyRep, opencv, scipy.

```bash
conda activate pyrep
pip install opencv-python scipy
cd Simulation/tasks/Kine_picking
python main.py
```

### Explanation of the main code

```python
# Import modules to be used in the project
from src.camera import Camera
from src.env import Env
from src.franka import Franka
```

Environment:

```python
# Load the environment file
env = Env('path to .ttt file')
# start simulation
env.start()
# stop simulation
env.stop()
# shutdown the v-rep GUI thread
env.shutdown()
```

Camera:

```python
# build Camera
cam = Camera()
# capture BGR image
img = cam.capture_bgr()
# capture Depth
depth = cam.capture_depth(in_meters=True)
```

Robot:

```python
# build franka
franka = Franka()
# move
franka.move(env,position,euler=euler)
# home
franka.home(env)
```
### TODO: your assignment

After complete the Kinematic Picking example, you are required to generate a path of waypoints for the robot so that the robot should draw the letters in "COVID-19" on the table. Each student pick one letter in "COVID-19". You should write your code in the TODO part in COVID-19.py. In the franka.move() function, the code will plot the path. So when the robot moves to all the waypoints, you should see the letter in the simulation window.

For example, the letter "C" can be seen as part of an ellipse curve. After specify the center, major axis and minor axis, you can obtain the path from the ellipse curve equation.

Please submit the following materials in one week:
  - A power point describing your project, 
  - A video of the simulation,
  - The COVID-19.py file.

## Project 2: Simulated Robot Player

To be released