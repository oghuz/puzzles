#! /usr/bin/python


from sklearn.ensemble import RandomForestClassifier
from sklearn import svm 
from numpy import genfromtxt, savetxt

def main():
    #create the training & test sets, skipping the header row with [1:]
    dataset = genfromtxt(open('./input/train.csv','r'), delimiter=',', dtype='f8')[1:]    
    target = [x[0] for x in dataset]
    train = [x[1:] for x in dataset]
    test = genfromtxt(open('./input/test.csv','r'), delimiter=',', dtype='f8')[1:]
    
    #create and train the random forest
    machine = svm.SVC(decision_function_shape='ovo')
    machine.fit(train, target)

    savetxt('output/svm.csv', machine.predict(test), delimiter=',', header =
            'ImageId,Label', fmt='%f')

if __name__=="__main__":
    main()


