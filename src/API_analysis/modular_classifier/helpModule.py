'''
@Saleem
help module for dangerous speech
'''

import sys
sys.dont_write_bytecode = True

#-----------------------------------------------------------------------------------------------
import re
import inflect
import pathModule

#-----------------------------------------------------------------------------------------------
#extended stop words
res_path = pathModule.resPath
stop1 = res_path+"stop.txt"
stop2 = res_path+"stopwords.txt"
stop3 = res_path+"smallstop.txt"

stopwords1 = set(line.strip() for line in open(stop1))
stopwords2 = set(line.strip() for line in open(stop2))
stopwords3 = set(line.strip() for line in open(stop3))
stopwords = stopwords1.union(stopwords2).union(stopwords3)

#-----------------------------------------------------------------------------------------------
def mergeSame(str1, str2):
        #return strings with more CAPS
	if str1 == str2:
                return str1
        elif upcount(str1) > upcount(str2):
                return str1
        else:
                return str2

def upcount(strtext):
	#return the number of CAPS
        count = 0
        regex = re.compile('[^a-zA-Z]')

        strtext = regex.sub('', strtext)
        lenstr = len(strtext)

        for x in strtext:
                if x.isupper():
                        count+=1

        if count == lenstr:
                return 0
        else:
                return count

def removePeriod(word):
        if '.' not in word:
                return word
        elif word[-1] == '.':
                return word[:-1]
        else:
                return word

def removeCaps(word):
        for z in word:
                if z.isupper():
                        return False
        return True

def mergePlural(lst):
        p = inflect.engine()

        newlist = []
        for item in lst:
                if p.singular_noun(item):
                        if p.singular_noun(item) not in newlist:
                                newlist.append(p.singular_noun(item))
                else:
                        if item not in newlist:
                                newlist.append(item)
        return newlist

def mkchunks(l, n):
        for i in xrange(0, len(l), n):
                yield l[i:i+n]

def readfile(filepath):
        #read a file
        with open(filepath, 'r') as fo:
                allines = fo.readlines()
        return allines

def write2file(filepath, l):
	with open(filepath, 'w') as fo:
                for item in l:
                        fo.write(item)
	return	

def sortTwo(l1, l2):
	z = sorted(zip(l1, l2))
	l1, l2 = zip(*z)
        return list(l1), list(l2)

def addTwo(l1, l2):
    	return [x[0] + x[1] for x in zip(l1, l2)]
