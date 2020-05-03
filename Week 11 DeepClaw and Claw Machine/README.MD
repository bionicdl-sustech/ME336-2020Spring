# Week 11 Introduction to DeepClaw

In week 11, students will learn the basic idea of Deepclaw. And then students are required to implement a smart claw machine in CoppeliaSim.

## DeepClaw basics

Please refer to the github repository of [DeepClaw](https://github.com/bionicdl-sustech/DeepClawBenchmark) for more information. 

DeepClaw is a benchmarking system for robot manipulation designed to be modularized, extendable, and easy to use on real robots and the environment, provided by the BionicDL lab at SUSTECH. Due to COVID-19, the students are not required to do their projects on real robots using DeepClaw. But you are encourage to read the github page and get familiar with the pipelines of robotic applications.

## Claw machine

![img](./Claw_machine.jpeg)

You have to program your franka robot to claw the toys in front of the robot and put toy to a box next to robot. Please refer to the readme under ME336/Simulation for more instructions on completing project 3.

[Here](./Claw_machine_presentation_1.mp4) is a example of this project

### pipeline of main loop

```python
while True:
    # capture image and depth-image
    # extract the ros(Region of interest in img)
    # resize the ros to 1280*720
    # call Deeplearning algorithm here, get best position,pose and possibility

    # if best possibility < 80%
        #break
    
    # compute from u,v and depth-image to real world position 
    # robot move pipeline
```
