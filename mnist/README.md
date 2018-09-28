# MNIST Dataset

## Purpose

Try out some neural network using the widely examined MNIST hand writting digits dataset.

## Data

* Data can be downloaded from Yann LeCun's website [THE MNIST DATABASE of handwritten digits](http://yann.lecun.com/exdb/mnist/) (not inlcuded in this repository). 
    * The function `read_mnist_data` in [helper.py](helper.py) can read these for datadets.   
* Perhaps more conveniently, it can be directly downloaded in a notebook using keras:

    ``` python 
    from keras.datasets import mnist
    (image_train, label_train), (image_test,label_test) = mnist.load_data() 
    ```
    This helps when running on colab (no need to upload data into the vm). 

## Notebooks

1. [data_exploration](data_exploration.ipynb): Plot a few data to check that the images and labels match correctly. 
2. [model_nn_keras.ipynb](model_nn_keras.ipynb): Plain neural network.
3. [model_cnn_keras.ipynb](model_cnn_keras.ipynb): Convolutional neural network


## Todo

* There's some problem when I try to use the imagenet-pretrained model. The validataion loss is constantly high while  training loss is down. Looks like overfitting?
