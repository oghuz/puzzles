#! /usr/bin/python


from sklearn.ensemble import RandomForestClassifier
from sklearn import svm 
import numpy as np 
from numpy import genfromtxt, savetxt

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
        conv1_num_filters=7, 
        conv1_filter_size=(3, 3), 
        conv1_nonlinearity=lasagne.nonlinearities.rectify,

        pool1_pool_size=(2, 2),

        conv2_num_filters=12, 
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
    dataset = np.genfromtxt(open('./input/train.csv','r'), delimiter=',',
                            dtype='uint8')[1:]    
    target = [x[0] for x in dataset]
    train = [x[1:] for x in dataset]
    test = genfromtxt(open('./input/test.csv','r'), delimiter=',', dtype='uint8')[1:]

    train = np.array(train).reshape((-1, 1, 28, 28)).astype(np.uint8)
    test = np.array(test).reshape((-1, 1, 28, 28)).astype(np.uint8)

    #create and train the random forest
    cnn = CNN(20).fit(train,target) # train the CNN model for 15 epochs

    np.savetxt('output/cnn.csv', cnn.predict(test), delimiter=',', header =
               'ImageId,Label', fmt='%f')

if __name__=="__main__":
    main()


