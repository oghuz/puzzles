#! /usr/bin/python
import numpy as np

from sklearn import svm 
from numpy import genfromtxt, savetxt

def main():
    #create the training & test sets, skipping the header row with [1:]
    dataset = genfromtxt(open('./input/train.csv','r'), delimiter=',', dtype='f8')[1:]    
    target = [x[0] for x in dataset]
    train = [x[1:] for x in dataset]
    test = genfromtxt(open('./input/test.csv','r'), delimiter=',', dtype='f8')[1:]
    
    #create and train the random forest
    machine = svm.SVC(verbose=True, decision_function_shape='ovo')
    machine.fit(train, target)
    pred = machine.predict(test)
    savetxt('submissions/svm.csv', np.c_[range(1,len(test)+1), pred], delimiter=',', header = 'ImageId,Label', comments = '', fmt='%d')


if __name__=="__main__":
    main()


