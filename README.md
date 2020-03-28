# ME336 Collaborative Robot Learning, Spring 2020 <!-- omit in toc -->

This repository is intended for the lab session of [ME336](https://ancorasir.com/?page_id=2320), created by [the Bionic Design and Learning Lab](https://ancorasir.com/) at [Southern University of Science and Technology](https://www.sustech.edu.cn/). Due to the COVID-19 situation, many of the content were modified so that the student can study remotely on their own laptop with a final session working with actual hardware. [This course was first offered during the Spring of 2019](https://ancorasir.com/?page_id=1310), and the majority of the lab session is carried out with various robotic hardware and a series of guest lecture series in robotics and AI. 
- Course Instructor
  - Prof. Song Chaoyang
  - Dr. Wan Fang
- Teaching Assistant
  - Mr. Liu Xiaobo
  - Mr. Ge Sheng

In the current version, the lab session feature four main components. 
- **Week 01~07**: The Missing Semester by MIT and Introduction to Python/TensorFlow/Ubuntu
- **Week 08~10**: Simulated Robot Player with PyRep
- **Week 11~13**: Arcade Claw Player with DeepClaw
- **Week 11~15**: Robot Learning Design Challenge on Autonomous Waste Sorting

## File Structure <!-- omit in toc -->
- **DeepClaw** (to be updated, a model zoo to streamline your program of robot learning developed by BionicDL@SUSTech)
- **Simulation** (to be updated, a simulation environment to help you guys getting started with robot learning)
- **Weekly Lab Folder** (detailed instructions for each week's lab content)

## Lab Arrangement <!-- omit in toc -->

- [Week 01~05 The Missing Semester by MIT](#week-0105-the-missing-semester-by-mit)
- [Week 06 Introduction to Python](#week-06-introduction-to-python)
- [Week 07 Introduction to TensorFlow](#week-07-introduction-to-tensorflow)
- [Week 08 Introduction to PyRep](#week-08-introduction-to-pyrep)
- [Week 09 MDP with Tic-Tac-Toe](#week-09-mdp-with-tic-tac-toe)
- [Week 10 Simulated Robot Player](#week-10-simulated-robot-player)
- [Week 11 Introduction to DeepClaw](#week-11-introduction-to-deepclaw)
- [Week 12 Arcade Claw Player](#week-12-arcade-claw-player)
- [Week 13 Waste Sorting Optimization](#week-13-waste-sorting-optimization)
- [Week 14 Interactive DesignAIR](#week-14-interactive-designair)
- [Week 15 Final Presentation](#week-15-final-presentation)

# [Week 01~05 The Missing Semester by MIT](Week%2001~05%20The%20Missing%20Semester%20by%20MIT/README.MD)

[The Missing Semester of Your CS Education](https://missing.csail.mit.edu/) by MIT CSAIL is a good starting point, if you are transitioning from an engineering background but unsure about programming. If you have trouble accessing Youtube, we have provided a copy of the video on OneDrive.

# [Week 06 Introduction to Python](Week%2006%20Introduction%20to%20Python/README.MD)

Python is a popular programming language that you can consider it as "executable pseudocode." In this lecture, you will practice basic installation with anaconda and setup the programming environment. You will also practice using it with Jupyter Notebook. An alternative is to use IDEs such as Microsoft VS code. You will also need to install Ubuntu 16.04 on your laptop to continue with the rest of the class.

# [Week 07 Introduction to TensorFlow](Week%2007%20Introduction%20to%20TensorFlow/README.MD)

TensorFlow is one of the most popular Deep learning frameworks, which offer building blocks for designing, training and validating deep neural networks, through a high level programming interface. In this lecture, you will install TensorFlow 2.x on your laptop with anaconda and go through a few tutorials on the basic usage of TensorFlow for deep learning.

# [Week 08 Introduction to PyRep](Week%2008%20Introduction%20to%20PyRep/README.MD)

PyRep is a version of V-rep with added support for reinforcement learning. V-rep recently changed its name to CoppeliaSim, which is a popular robot simulator used widely in academics and applications. Robot learning task relies heavily on simulation due to the fact that robots are relatively expensive to buy and time-consuming to setup. In this lecture, you will learn the basic usage of PyRep, and learn how to set it up for robot learning on basic vision-based picking tasks.

# [Week 09 MDP with Tic-Tac-Toe](Week%2009%20MDP%20with%20Tic-Tac-Toe/README.MD)

Tic-Tac-Toe is such a classic that you just can't miss when learning about games. You probably learned in the past on how to program Tic-Tac-Toe with MINIMAX or other methods. In this class, we will set it up as a Markove Decision Process (MDP) and see how we can "hack" a virtual player that "almost" always wins using reinforcement learning

# [Week 10 Simulated Robot Player](Week%2010%20Simulated%20Robot%20Player/README.MD)

Playing on the screen within the terminal is just ... boring. How about implementing Tic-Tac-Toe with a simulated robot player that plays against you on a game board? (We originally intended to have you guys practise this part with physical robots like the students did in the last semeters. Due to the the COVID-19 situation, we are left with very limited time to prepare this part for you. But I hope the simulated robot player will still give you the excitement to carry on with the learning.) You will also learn some of the challenges with robot learning when dealing with a "real" robot hardware, and take a look at gap between simulation and reality.

# [Week 11 Introduction to DeepClaw](Week%2011%20Introduction%20to%20DeepClaw/README.MD)

In this lecture, let's practice robot learning for real with [DeepClaw](https://github.com/bionicdl-sustech/DeepClawBenchmark). DeepClaw is a streamlined model zoo for robot learning that is developed at the Bionic Design and Learning Lab. Through this lecture, we will teach you a pipeline of implementing robot learning with examples from DeepClaw. Later, you will use DeepClaw to build a waste sorting robot with deep learning.

# [Week 12 Arcade Claw Player](Week%2012%20Arcade%20Claw%20Player/README.MD)

Practice, practice, and practice. Let's just try working through a simple example on building an arcade claw robot from scratch to get familiar with the hardware and software details (so that you don't break the robot, and more importantly, injure yourself). You will use a neural network trained with a robot picking stuffed toys can get a feeling about how you can build a waste sorting robot on your own. Also, you should really get started with training your own waste sorting neural network for your final project. 

# [Week 13 Waste Sorting Optimization](Week%2013%20Waste%20Sorting%20Optimization/README.MD)

This week's focus is on optimizing your trained neural network for autonomous waste sorting. We are still working on this part and will update with more details later.

# [Week 14 Interactive DesignAIR](Week%2014%20Interactive%20DesignAIR/README.MD)

While preparing your final presentation, let's work together on a little experiment based on a research collaboration on new engineering education between SUSTech and MIT. You will play with a system developed at the Bionic Design and Learning Lab @ SUSTech called DesignAIR and share your feedback on your experience in new engineering education with it.

# [Week 15 Final Presentation](Week%2015%20Final%20Presentation/README.MD)

This is THE moment, as you will present your final presentation on the Robot Learning Challenge of designing a Waste Sorting Robot and share with the class of your latest development. We will also try to squeeze in a guest lecture in today's class (we will definitely try).
