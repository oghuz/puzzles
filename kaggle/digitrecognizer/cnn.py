#! /usr/local/bin/python

import lasagne
import numpy as np 
import nolearn
import theano 

from numpy import genfromtxt, savetxt

from nolearn.lasagne import NeuralNet
from nolearn.lasagne import TrainSplit
from nolearn.lasagne import objective
from nolearn.lasagne import BatchIterator

from lasagne import layers
from lasagne.layers import DenseLayer
from lasagne.layers import InputLayer
from lasagne.layers import DropoutLayer
from lasagne.layers import Conv2DLayer
from lasagne.layers import MaxPool2DLayer
from lasagne.nonlinearities import softmax
from lasagne.updates import adam
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


class FlipBatchIterator(BatchIterator):
  flip_indices = [
      (0, 2), (1, 3),
      (4, 8), (5, 9), (6, 10), (7, 11),
      (12, 16), (13, 17), (14, 18), (15, 19),
      (22, 24), (23, 25),
      ]

  def transform(self, Xb, yb):
    Xb, yb = super(FlipBatchIterator, self).transform(Xb, yb)
    # Flip half of the images in this batch at random:
    bs = Xb.shape[0]
    indices = np.random.choice(bs, bs / 2, replace=False)
    Xb[indices] = Xb[indices, :, :, ::-1]

    if yb is not None:
      # Horizontal flip of all x coordinates:
      yb[indices, ::2] = yb[indices, ::2] * -1
      # Swap places, e.g. left_eye_center_x -> right_eye_center_x
      for a, b in self.flip_indices:
        yb[indices, a], yb[indices, b] = (yb[indices, b], yb[indices, a])
    return Xb, yb


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

def CNN0(n_epochs):
  layers0 = [
      # layer dealing with the input data
      (InputLayer, {'shape': (None, 1,28,28)}),

      # first stage of our convolutional layers
      (Conv2DLayer, {'num_filters': 96, 'filter_size': 5}),
      (Conv2DLayer, {'num_filters': 96, 'filter_size': 3}),
      (Conv2DLayer, {'num_filters': 96, 'filter_size': 3}),
      (Conv2DLayer, {'num_filters': 96, 'filter_size': 3}),
      (Conv2DLayer, {'num_filters': 96, 'filter_size': 3}),
      (MaxPool2DLayer, {'pool_size': 2}),

      # second stage of our convolutional layers
      (Conv2DLayer, {'num_filters': 128, 'filter_size': 3}),
      (Conv2DLayer, {'num_filters': 128, 'filter_size': 3}),
      (Conv2DLayer, {'num_filters': 128, 'filter_size': 3}),
      (MaxPool2DLayer, {'pool_size': 2}),

      # two dense layers with dropout
      (DenseLayer, {'num_units': 64}),
      (DropoutLayer, {}),
      (DenseLayer, {'num_units': 64}),

      # the output layer
      (DenseLayer, {'num_units': 10, 'nonlinearity': softmax}),
      ]

  net0 = NeuralNet(
      layers=layers0,
      max_epochs=n_epochs,

      update=adam,
      update_learning_rate=0.0002,

      objective=regularization_objective,
      objective_lambda2=0.0025,

      train_split=TrainSplit(eval_size=0.25),
      verbose=1,
      )
  return net0


def CNN6(n_epochs):
  net6 = NeuralNet(
      layers=[
        ('input', layers.InputLayer),
        ('conv1', layers.Conv2DLayer),
        ('pool1', layers.MaxPool2DLayer),
        ('dropout1', layers.DropoutLayer),  # !
        ('conv2', layers.Conv2DLayer),
        ('pool2', layers.MaxPool2DLayer),
        ('dropout2', layers.DropoutLayer),  # !
        ('conv3', layers.Conv2DLayer),
        ('pool3', layers.MaxPool2DLayer),
        ('dropout3', layers.DropoutLayer),  # !
        ('hidden4', layers.DenseLayer),
        ('dropout4', layers.DropoutLayer),  # !
        ('hidden5', layers.DenseLayer),
        ('output', layers.DenseLayer),
        ],
      input_shape=(None, 1, 28, 28),
      conv1_num_filters=32, conv1_filter_size=(3, 3), pool1_pool_size=(2, 2),
      dropout1_p=0.1,  # !
      conv2_num_filters=64, conv2_filter_size=(2, 2), pool2_pool_size=(2, 2),
      dropout2_p=0.2,  # !
      conv3_num_filters=128, conv3_filter_size=(2, 2), pool3_pool_size=(2, 2),
      dropout3_p=0.3,  # !
      hidden4_num_units=500,
      dropout4_p=0.5,  # !
      hidden5_num_units=500,
      output_num_units=10, 
      output_nonlinearity=lasagne.nonlinearities.softmax,

      update_learning_rate=theano.shared(float32(0.0001)),
      update_momentum=theano.shared(float32(0.9)),
      batch_iterator_train=FlipBatchIterator(batch_size=128),
      on_epoch_finished=[
        AdjustVariable('update_learning_rate', start=0.03, stop=0.0001),
        AdjustVariable('update_momentum', start=0.9, stop=0.999),
        ],
      max_epochs=n_epochs,
      verbose=1,
      )
  return net6

def CNN(n_epochs):
  net1 = NeuralNet(
      layers=[
        ('input', layers.InputLayer),
        ('conv1', layers.Conv2DLayer),      #Convolutional layer.  Params defined below
        ('pool1', layers.MaxPool2DLayer),   # Like downsampling, for execution speed
        ('conv2', layers.Conv2DLayer),
        ('hidden3', layers.DenseLayer),
        ('output', layers.DenseLayer),
        ],

      input_shape=(None, 1, 28, 28),
      conv1_num_filters=32, 
      conv1_filter_size=(3, 3), 
      conv1_nonlinearity=lasagne.nonlinearities.rectify,
      pool1_pool_size=(2, 2),

      conv2_num_filters=64, 
      conv2_filter_size=(2, 2),    
      conv2_nonlinearity=lasagne.nonlinearities.rectify,

      hidden3_num_units=1000,
      output_num_units=10, 
      output_nonlinearity=lasagne.nonlinearities.softmax,

      update_learning_rate=0.0001,
      update_momentum=0.9,

      max_epochs=n_epochs,
      verbose=1,
      )

  return net1




def main():
  #create the training & test sets, skipping the header row with [1:]
    print "Reading input files .. "
    dataset = genfromtxt(open('./input/train.csv','r'), delimiter=',',
        dtype='uint8')[1:]    
    test = genfromtxt(open('./input/test.csv','r'), delimiter=',', dtype='uint8')[1:]

    print "Transforming input files .. "
    target = np.array([x[0] for x in dataset]).astype(np.uint8)
    train = np.array([x[1:] for x in dataset]).reshape((-1, 1, 28, 28)).astype(np.float32)
    test = np.array(test).reshape((-1, 1, 28, 28)).astype(np.uint8)

    print "Training DeepNet .. "    
    cnn = CNN0(200).fit(train,target)
    pred = cnn.predict(test)

    savetxt('submissions/cnn6.csv', np.c_[range(1,len(test)+1),pred], delimiter=',', header = 'ImageId,Label', comments = '', fmt='%d')

if __name__=="__main__":
  main()


