'''
@Saleem
data pipeline for dangerous speech
'''

import sys
sys.dont_write_bytecode = True

#-----------------------------------------------------------------------------------------------
import loadModule
import helpModule
import trainModule
import testModule
import metricsModule
import sys
from operator import add
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

#-----------------------------------------------------------------------------------------------
trainsource = 'reddit'
algo = 'lr'
trainpos = sys.argv[1]
trainneg = 'random'
#testsource = sys.argv[6]
#testfile = sys.argv[7]

#-----------------------------------------------------------------------------------------------
# load training data
print '>loading training data'
trainposlines = loadModule.loadData(trainsource, trainpos)
trainneglines = loadModule.loadData(trainsource, trainneg)

# subsample training data
print '>subsampling training data'
trainposlines, trainneglines = loadModule.subsampleData(
    trainposlines, trainneglines)

# generate training set
print '>generating training dataset'
traindata = []
traintarget = []

data, target = loadModule.genData(trainposlines, 0)
print len(data), len(target)
traindata.extend(data)
traintarget.extend(target)

data, target = loadModule.genData(trainneglines, 1)
print len(data), len(target)
traindata.extend(data)
traintarget.extend(target)

traindata, traintarget = helpModule.sortTwo(traindata, traintarget)

print '>unlabelled classification'

# train data
print '>training the model', algo
clf, count_vect, tfidf_transformer = trainModule.training(
    traindata, traintarget, algo)

'''
#load testing data
print '>loading testing data'
testlines = loadModule.loadData(testsource, testfile)

#generate testing set
print '>generating testing dataset'

testdata, testtarget = loadModule.unlablledData(testlines)

#testing the data
print '>testing the model'
predicted = testModule.testing(testdata, clf, count_vect, tfidf_transformer)

#results
indices = []
for i in zip(predicted, testtarget):
        if i[0] == 0:
                indices.append(i[1])

to_write = metricsModule.aggregateLab(testlines, indices)

#writing labelled content
print '>writing to file'
helpModule.write2file('labelled.txt', to_write)
'''
