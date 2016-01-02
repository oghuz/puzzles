#! /usr/local/bin/python

import lasagne
import numpy as np 
import nolearn
import theano 
import cPickle as pickle

from numpy import genfromtxt, savetxt

from nolearn.lasagne import NeuralNet
from nolearn.lasagne import TrainSplit
from nolearn.lasagne import objective

from lasagne import layers
from lasagne.layers import DenseLayer
from lasagne.layers import InputLayer
from lasagne.layers import DropoutLayer
from lasagne.layers import Conv2DLayer
from lasagne.layers import MaxPool2DLayer
from lasagne.nonlinearities import softmax
from lasagne.updates import adam
from lasagne.updates import nesterov_momentum
from lasagne.layers import get_all_params

def float32(k):
    return np.cast['float32'](k)

class AdjustVariable(object):
    def __init__(self, name, start=0.03, stop=0.001):
        self.name = name
        self.start, self.stop = start, stop
        self.ls = None
    def __call__(self, nn, train_history):
        if self.ls is None:
            self.ls = np.linspace(self.start, self.stop, nn.max_epochs)
        epoch = train_history[-1]['epoch']
        new_value = float32(self.ls[epoch - 1])
        getattr(nn, self.name).set_value(new_value)

def regularization_objective(layers, lambda1=0., lambda2=0., *args, **kwargs):
    # default loss
    losses = objective(layers, *args, **kwargs)
    # get the layers' weights, but only those that should be regularized
    # (i.e. not the biases)
    weights = get_all_params(layers[-1], regularizable=True)
    # sum of absolute weights for L1
    sum_abs_weights = sum([abs(w).sum() for w in weights])
    # sum of squared weights for L2
    sum_squared_weights = sum([(w ** 2).sum() for w in weights])
    # add weights to regular loss
    losses += lambda1 * sum_abs_weights + lambda2 * sum_squared_weights
    return losses

def simpleCNN():
    layers0 = [
        # layer dealing with the input data
        (InputLayer, {'shape': (None, 1,28,28)}),

        # first stage of our convolutional layers
        (Conv2DLayer, {'num_filters': 16, 'filter_size': 2}),
        (DenseLayer, {'num_units': 64}),

        # the output layer
        (DenseLayer, {'num_units': 10, 'nonlinearity': softmax}),
    ]

    net0 = NeuralNet(
        layers=layers0,
        update=nesterov_momentum,
        update_learning_rate = theano.shared(float32(0.01)),
        update_momentum = theano.shared(float32(0.9)),
        on_epoch_finished=[
            AdjustVariable('update_learning_rate', start=0.03, stop=0.0001),
            AdjustVariable('update_momentum', start=0.9, stop=0.999),
        ],

        verbose=1,
    )
    return net0

def CNN0(n_epochs):
    layers0 = [
        # layer dealing with the input data
        (InputLayer, {'shape': (None, 1,28,28)}),

        # first stage of our convolutional layers
        (Conv2DLayer, {'num_filters': 96, 'filter_size': 5}),
        (MaxPool2DLayer, {'pool_size': 2}),
        (Conv2DLayer, {'num_filters': 96, 'filter_size': 3}),

        # second stage of our convolutional layers
        (Conv2DLayer, {'num_filters': 128, 'filter_size': 3}),
        (MaxPool2DLayer, {'pool_size': 2}),
        (Conv2DLayer, {'num_filters': 128, 'filter_size': 3}),

        # two dense layers with dropout
        (DenseLayer, {'num_units': 128}),
        (DenseLayer, {'num_units': 64}),

        # the output layer
        (DenseLayer, {'num_units': 10, 'nonlinearity': softmax}),
    ]

    net0 = NeuralNet(
        layers=layers0,
        max_epochs=n_epochs,

        update_learning_rate=0.0002,

        objective=regularization_objective,
        objective_lambda2=0.0025,
        verbose=1,
    )
    return net0


def CNN(n_epochs):
    net6 = NeuralNet(
        layers=[
            ('input', layers.InputLayer),
            ('conv1', layers.Conv2DLayer),
            ('pool1', layers.MaxPool2DLayer),
            ('conv2', layers.Conv2DLayer),
            ('dropout1', layers.DropoutLayer),  # !
            ('conv3', layers.Conv2DLayer),
            ('pool2', layers.MaxPool2DLayer),
            ('conv4', layers.Conv2DLayer),
            ('dropout2', layers.DropoutLayer),  # !
            ('hidden4', layers.DenseLayer),
            ('hidden5', layers.DenseLayer),
            ('output', layers.DenseLayer),
        ],
        input_shape=(None, 1, 28, 28),
        
        conv1_num_filters=96, conv1_filter_size=(5,5),
        pool1_pool_size=(2, 2),
        conv2_num_filters=96, conv2_filter_size=(3, 3), 
        dropout1_p=0.1,  # !
        
        conv3_num_filters=128, conv3_filter_size=(3, 3),
        pool2_pool_size=(2, 2),
        conv4_num_filters=128, conv4_filter_size=(3, 3), 
        dropout2_p=0.1,  # !
        
        hidden4_num_units=128,
        hidden5_num_units=64,
        output_num_units=10, 
        output_nonlinearity=lasagne.nonlinearities.softmax,

        update_learning_rate = float32(0.001),
        update_momentum = float32(0.9),
        max_epochs=n_epochs,
        verbose=1,
    )
    return net6

def load():
    import os.path

    if os.path.exists('./input/train.pickle') and os.path.exists('./input/target.pickle'):
        print "Loading from train examples from pickles .."
        with open('./input/train.pickle', 'rb') as f:
            train = pickle.load(f)
            with open('./input/target.pickle', 'rb') as f:
                target = pickle.load(f)
    else:
        print "Reading input files .. "
        dataset = genfromtxt(open('./input/train.csv','r'), delimiter=',', dtype='uint8')[1:]
        print "Transforming input files .. "
        target = np.array([x[0] for x in dataset]).astype(np.uint8)
        train = np.array([x[1:] for x in dataset]).reshape((-1, 1, 28, 28)).astype(np.float32)
        print "Dumping pickles .. "
        with open('./input/target.pickle', 'wb') as f:
            pickle.dump(target, f, -1)
            with open('./input/train.pickle', 'wb') as f:
                pickle.dump(train, f, -1)

    print "Loading test file .." 
    if os.path.exists('./input/test.pickle'):
        with open('./input/test.pickle', 'rb') as f:
            test= pickle.load(f)
    else:
        test = genfromtxt(open('./input/test.csv','r'), delimiter=',', dtype='uint8')[1:]
        test = np.array(test).reshape((-1, 1, 28, 28)).astype(np.uint8)
        with open('./input/test.pickle', 'wb') as f:
            pickle.dump(test, f, -1)
    
    return train,target,test

def dumpModel(cnn):
    with open('./models/cnn.pickle', 'wb') as f:
        pickle.dump(cnn, f, -1)

def main():
    train,target,test = load()

    print "Training DeepNet .. "    
    #cnn = CNN0(10).fit(train,target)
    cnn = simpleCNN().fit(train,target)

    print "Predicting Labels .. "    
    pred = cnn.predict(test)
    savetxt('submissions/cnn.2conv.csv', np.c_[range(1,len(test)+1),pred], delimiter=',', header = 'ImageId,Label', comments = '', fmt='%d')

    print "Pickling DeepNet model.. "    
    dumpModel(cnn)

if __name__=="__main__":
    main()


