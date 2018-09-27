import struct
import os
import numpy as np

# see http://yann.lecun.com/exdb/mnist/ for data format

def read_mnist_label_file(path):
    with open(path, 'rb') as f:
        byte = f.read() 
        magic_number = struct.unpack_from('>I', byte)[0]
        num_item = struct.unpack_from('>I', byte, offset=4)[0]
        itr = struct.iter_unpack('B', byte[8:])
        labels = np.array([item for item in itr])
        if magic_number != 2049 or labels.shape[0] != num_item:
            print("Something is wrong!")
    return labels 

def read_image_file(path):
    with open(path, 'rb') as f:
        byte = f.read() 
        (magic_number, num_item, num_row, num_col) = struct.unpack_from('>IIII', byte)
        image_size = (num_row, num_col)
        itr = struct.iter_unpack('B'*image_size[0]*image_size[1], byte[16:])
        images = np.array([item for item in itr])
        if magic_number != 2051 or images.shape[0] != num_item or image_size != (28, 28):
            print("Something is wrong!")
    return images, image_size 

def read_mnist_data(data_path):
    label_train = read_mnist_label_file(os.path.join(data_path, 'train-labels-idx1-ubyte'))
    image_train, image_size_train = read_image_file(os.path.join(data_path, 'train-images-idx3-ubyte'))
    label_test = read_mnist_label_file(os.path.join(data_path, 't10k-labels-idx1-ubyte'))
    image_test, image_size_test = read_image_file(os.path.join(data_path, 't10k-images-idx3-ubyte'))
    return image_train, label_train, image_test, label_test
                                           


