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
from sklearn.cross_validation import KFold
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.utils import shuffle

print '>pipeline specs'
print '\t'.join([str(x) for x in sys.argv])
#-----------------------------------------------------------------------------------------------
trainsource = sys.argv[1]
crossval = sys.argv[2]
algo = sys.argv[3]
trainpos = sys.argv[4]
trainneg = sys.argv[5]

#-----------------------------------------------------------------------------------------------
#load training data
print '>loading training data'
trainposlines = loadModule.loadData(trainsource, trainpos)
trainneglines = loadModule.loadData(trainsource, trainneg)

#subsample training data
print '>subsampling training data'
trainposlines, trainneglines = loadModule.subsampleData(trainposlines, trainneglines)

#generate training set
print '>generating training dataset'
traindata = []
traintarget = []

data, target = loadModule.genData(trainposlines, 0)
traindata.extend(data)
traintarget.extend(target)

data, target = loadModule.genData(trainneglines, 1)
traindata.extend(data)
traintarget.extend(target)

traindata, traintarget = shuffle(traindata, traintarget)
print len(traintarget)

if crossval == '10fold':
	print '>ten fold classification'
	
	#cross validation
	print '>splitting the dataset'
	num = len(traindata)
	kf = KFold(num, n_folds=10)

	index = 0
	results = [0,0,0,0,0]	

        scorefile = 'score_'+trainpos+'.txt'

	for train, test in kf:
		index+=1
		
		#training data
		'>training set'
		trainingdata = [traindata[i] for i in train]
		trainingtarget = [traintarget[i] for i in train]		
	
		#testing data
		'>testing set'
		testingdata = [traindata[i] for i in test]
                testingtarget = [traintarget[i] for i in test]	
		predicted = []

                #train data
                '>training the model', algo
                clf, count_vect, tfidf_transformer = trainModule.training(trainingdata, trainingtarget, algo)	

                #testing the data
                '>testing the model'
                idlist, predicted = testModule.testing(testingdata, clf, count_vect, tfidf_transformer)
                with open(scorefile, 'a') as fout:
                    for item in zip(idlist, predicted):
                        fout.write(str(item[0])+' '+str(item[1])+'\n')

                #performance
                if index == 1:
                        print '>performance'
                        metricsModule.printHead()
                fold_results = metricsModule.getScore(testingtarget, predicted)
                results = helpModule.addTwo(results, fold_results)
        print '\t'.join(['----','----','----','----', '----'])
        print '\t'.join([str(round(x/10, 2)) for x in results])
