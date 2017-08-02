'''
@Saleem
load module for dangerous speech
'''

import sys
sys.dont_write_bytecode = True

#-----------------------------------------------------------------------------------------------
import pathModule
import json
import os
import preprocessModule
import math

#-----------------------------------------------------------------------------------------------


def subsampleData(poslines, neglines):

    negnum = len(neglines)
    posnum = len(poslines)
    samplesize = min(posnum, negnum)
    # if samplesize > 1000:
    #	samplesize = int(math.floor(samplesize / 1000.0)) * 1000

    # if samplesize > 10000:
    #       samplesize = 10000

    possample = poslines[:samplesize]
    negsample = neglines[:samplesize]

    print len(possample), len(negsample)
    return possample, negsample


def loadData(source, target):
    target = target + '.txt'
    data_path = pathModule.dataPath + source + '/'

    if source == 'voat':
        data_path = data_path + 'data/'

    filepath = os.path.join(data_path, target)

    with open(filepath, 'r') as fo:
        lines = fo.readlines()

    return_data = []

    if source == 'reddit' or source == 'unbalance2' or source == 'camready' or source == 'unbalance':
        for line in lines:
            cmtjson = json.loads(line)
            text = cmtjson['body']
            return_data.append(text)

    elif source == 'twitter':
        for line in lines:
            cmtjson = json.loads(line)
            text = cmtjson['text']
            return_data.append(text)
    else:
        return_data = lines

    return return_data


def genData(lines, label):
    # data arrays
    data = []
    target = []

    for text in lines:
        if preprocessModule.cleanUp(text):
            data.append(preprocessModule.cleanUp(text))
            target.append(label)

    return data, target


def unlablledData(lines):
    # data arrays
    data = []
    target = []

    for i in xrange(len(lines)):
        if preprocessModule.cleanUp(lines[i]):
            data.append(preprocessModule.cleanUp(lines[i]))
            target.append(i)

    return data, target
