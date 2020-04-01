# Week 07 Introduction to TensorFlow  <!-- omit in toc -->
In today's lab session, we will introduce some widely used deep learning frameworks. Among them, we adopt tensorflow as the frame for ME336. We will go through two tutorials, mnist tutorial from google's course "Tensorflow Without a PhD" and fashion-mnist from tensorflow's official documentation.

- [Deep Learning Frameworks:](#deep-learning-frameworks)
- [TensorFlow Tutorial-1: Tensorflow Without a PhD](#tensorflow-tutorial-1-tensorflow-without-a-phd)
- [TensorFlow Tutorial-2: Fasion mnist](#tensorflow-tutorial-2-fasion-mnist)

## [Deep Learning Frameworks](https://developer.nvidia.com/deep-learning-frameworks):
 Deep learning frameworks offer building blocks for designing, training and validating deep neural networks, through a high level programming interface. Following is a list of popular deep learning frameworks:
  - [PyTorch](https://pytorch.org/): PyTorch is a GPU accelerated tensor computational framework with a Python front end.
  - [MXNet](http://mxnet.incubator.apache.org/get_started?): MXNet is a deep learning framework designed for both efficiency and flexibility. It allows you to mix the flavors of symbolic programming and imperative programming to maximize efficiency and productivity.
  - [TensorFlow](https://docs.nvidia.com/deeplearning/frameworks/tensorflow-user-guide/index.html): TensorFlow is an open-source software library for numerical computation using data flow graphs.

  - [MATLAB](https://www.mathworks.com/solutions/deep-learning.html): MATLAB makes deep learning easy for engineers, scientists and domain experts. With tools and functions for managing and labeling large data sets, MATLAB also offers specialized toolboxes for working with machine learning, neural networks, computer vision, and automated driving.
  - [NVIDIA Caffe](https://docs.nvidia.com/deeplearning/frameworks/caffe-user-guide/index.html): NVCaffe<sup>TM</sup> is an NVIDIA-maintained fork of  the [Berkeley Vision and Learning Center (BVLC)](http://caffe.berkeleyvision.org/) Caffe tuned for NVIDIA GPUs, particularly in multi-GPU configurations.
  - [Chainer](https://chainer.org/): Chainer is a Python-based deep learning framework aiming at flexibility.
  - [PaddlePaddle](https://www.paddlepaddle.org.cn/): PaddlePaddle provides an intuitive and flexible interface for loading data and specifying model structures. It supports CNN, RNN, multiple variants and configures complicated deep models easily.

  ## TensorFlow Tutorial-1: Tensorflow Without a PhD
  Tensorflow and deep learning without a PhD series is a crash course in six episodes for software developers who want to learn machine learning, with examples, theoretical concepts, and engineering tips, tricks and best practices to build and train the neural networks that solve your problems. All the resources including video, slides, code can be found on the [github page](https://github.com/GoogleCloudPlatform/tensorflow-without-a-phd).

  In order to have a clearer idea of constructing neural network in tensorflow, it is recommended to use their earlier codes, which is also explained in their slides. The earlier codes is compatible with tensorflow 1.15. Note the software version compatibility is a issue we will face often, that the reason we use anaconda. Please follow the following instructions to set the environment:

  ```bash
  # Create a conda environment with tensorflow 1.15
  conda create --name tf1.15 python=3.7
  conda activate tf1.15
  pip install tensorflow==1.15 matplotlib==3.0.3
  ```

  Go to the ME336 foler and update to the lastest code. For this week, the students are required to go through mnist_1.0_softmax.py first, which corresponds to the first 16 pages in the [slide](https://www.slideshare.net/albertspijkers/martin-gorner-tensorflow-and-deep-learning-without-a-phd). We will cover the other examples in the following week.
  ```bash
  # Pull the lastest ME336 code
  cd DesignAIR-ME336
  git pull
  cd  Week 07 Introduction to TensorFlow/tensorflow-without-a-phd/tensorflow-mnist-tutorial

  # Run the example
  python mnist_1.0_softmax.py
  ```

  Deactivate the tf1.15 environment when finish the tutorial
  ```bash
  conda deactivate
  ```

  ## TensorFlow Tutorial-2: Fasion mnist

  Fashion-MNIST is a dataset consisting of a training set of 60,000 examples and a test set of 10,000 examples. Please go to the [github page](https://github.com/zalandoresearch/fashion-mnist#get-the-data) for more detailed information. The Fasion mnist code is already included in ME336 and can be run with tensorflow 2.0. Follow the instructions below to install and run it in a new environment.
  ```bash
  # Create a conda environment with tensorflow 1.15
  conda create --name tf2.0 python=3.7
  conda activate tf2.0
  pip install tensorflow==2.0 matplotlib

  # Install the following package so that you can use tf2.0 in jupyter notebook
  conda install nb_conda_kernels

  # Run jupyter notebook, and remember to choose tf2.0 as the kernal after you open Fashion_mnist.ipynb
  cd DesignAIR-ME336/Week 07 Introduction to TensorFlow
  jupyter notebook
  ```
 
  **Note:** If you don't see you tf2.0 environment in jupyter notebook, please follow the [instructions in week 6](https://github.com/bionicdl-sustech/ME336/tree/master/Week%2006%20Introduction%20to%20Python#environment-in-jupyter-notebook).

<!--
- [TensorFlow Basics](https://www.guru99.com/tensor-tensorflow.html): Tensor, Shape, Type, Graph, Sessions & Operators
- Tutorials: the examples are handwritten digits classification and image classification. The datasets used is [MNIST]((http://yann.lecun.com/exdb/mnist/)) and [FASHION MNIST](https://github.com/zalandoresearch/fashion-mnist#get-the-data), and they have been downloaded as mnist.npz and Fashion-MNIST in week07 folder.

## TensorFlow Installation
As [TensorFlow](https://pytorch.org/get-started/locally/#windows-anaconda)=2.x is not available from conda, we use pip to install it.
> ``pip install tensorflow==2.0``
> #if it's too slow, use other source like below    
> ``pip install tensorflow==2.0 -ihttps://pypi.tuna.tsinghua.edu.cn/simple/``

## TensorFlow Basic
Follow this [page](https://www.guru99.com/tensor-tensorflow.html) for a qucik overview of tensorflow basics. In this tutorial, you will learn:
- [What is a Tensor?](https://www.guru99.com/tensor-tensorflow.html#1)
- [Representation of a Tensor](https://www.guru99.com/tensor-tensorflow.html#2)
- [Types of Tensor](https://www.guru99.com/tensor-tensorflow.html#3)
- [Create a tensor of n-dimension](https://www.guru99.com/tensor-tensorflow.html#4)
- [Shape of tensor](https://www.guru99.com/tensor-tensorflow.html#5)
- [Type of data](https://www.guru99.com/tensor-tensorflow.html#6)
- [Creating operator](https://www.guru99.com/tensor-tensorflow.html#7)
- [Some Useful TensorFlow operators](https://www.guru99.com/tensor-tensorflow.html#8)
- [Variables](https://www.guru99.com/tensor-tensorflow.html#9)
- [Placeholder](https://www.guru99.com/tensor-tensorflow.html#10)
- [Session](https://www.guru99.com/tensor-tensorflow.html#11)
- [Graph](https://www.guru99.com/tensor-tensorflow.html#12)

## TensorFlow Tutorials
The official tutorial of tensorflow is [here](https://www.tensorflow.org/tutorials). And we also get some quick starts:
- **[mnist](http://yann.lecun.com/exdb/mnist/)**: run the [mnist.ipynb](./mnist.ipynbb). You can also refer to this [link](https://www.tensorflow.org/tutorials/quickstart/beginner).
- **[Fashion_mnist](https://github.com/zalandoresearch/fashion-mnist#get-the-data)**: Install matplotlib first as we need show figures ``conda install -c conda-forge matplotlib``; then run the [Fashion_mnist.ipynb](./Fashion_mnist.ipynb). You can also refer to this [link](https://www.tensorflow.org/tutorials/keras/classification).
-->
