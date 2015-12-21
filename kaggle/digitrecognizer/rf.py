#! /usr/bin/python


from sklearn.ensemble import RandomForestClassifier
from numpy import genfromtxt, savetxt

def main():
    #create the training & test sets, skipping the header row with [1:]
    dataset = genfromtxt(open('./input/train.csv','r'), delimiter=',', dtype='f8')[1:]    
    target = [x[0] for x in dataset]
    train = [x[1:] for x in dataset]
    test = genfromtxt(open('./input/test.csv','r'), delimiter=',', dtype='f8')[1:]
    
    #create and train the random forest
    rf = RandomForestClassifier(n_estimators=100, n_jobs=8)
    rf.fit(train, target)

    #savetxt('Data/submission2.csv', rf.predict(test), delimiter=',', fmt='%f')
    savetxt('output/submission_rand_forest.csv', np.c_[range(1,len(test)+1),pred], delimiter=',', header = 'ImageId,Label', comments = '', fmt='%d')

if __name__=="__main__":
    main()


