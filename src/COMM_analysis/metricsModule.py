'''
@Saleem
load module for dangerous speech
'''

import sys
sys.dont_write_bytecode = True

#-----------------------------------------------------------------------------------------------
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import confusion_matrix

#-----------------------------------------------------------------------------------------------


def getScore(true, predicted):
    z = list(precision_recall_fscore_support(
        true, predicted, average='binary', pos_label=0))[:-1]
    acc = accuracy_score(true, predicted)
    confusion = confusion_matrix(true, predicted)
    k = kappa(confusion[0, 0], confusion[0, 1],
              confusion[1, 0], confusion[1, 1])
    res = [acc, z[0], z[1], z[2], k]
    print '\t'.join([str(round(x, 2)) for x in res])
    return res


def printHead():
    print '\t'.join(['Acc', 'Pre', 'Rec', 'F1', 'Kappa'])
    return


def aggregateLab(lines, indices):
    returnlist = []
    for index in indices:
        returnlist.append(lines[index])
    return returnlist


def kappa(a, b, c, d):
    tot = a + b + c + d
    Pa = float(a + d) / tot
    PA1 = float(a + b) / tot
    PA2 = 1.0 - PA1
    PB1 = float(a + c) / tot
    PB2 = 1.0 - PB1
    Pe = PA1 * PB1 + PA2 * PB2
    return (Pa - Pe) / (1.0 - Pe)
