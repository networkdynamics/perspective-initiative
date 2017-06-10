'''
Joining the results from Perspective and Community-classifier
Bin the Reddit comments based on the combined results

@Saleem
June 6, 2017
'''

#IMPORTS
import sys
import os

#DATA SETTINGS
data_path = '/home/ndg/users/hsalee/perspective-initative/data/classifier/'
target = sys.argv[1]

class_file = os.path.join(data_path, 'classifier_'+target+'.txt')
persp_file = os.path.join(data_path, 'perspective_'+target+'.txt')

with open(class_file, 'r') as fin:
    class_score = fin.readlines()
with open(persp_file, 'r') as fin:
    pers_score = fin.readlines()

#CLASSIFIER RESULT TO DICT
class_score_dict = {}
for line in class_score:
    line_1 = line.strip().split()
    class_score_dict[line_1[0]] = int(line_1[1])

#COMBINED SCORE
final_score = []
for line in pers_score:
    if 'ERROR' not in line:
        cid = line.split()[0]
        score = float(line.split()[1])
        if cid in class_score_dict:
            final_score.append([cid, score, class_score_dict[cid]])




bin_1 = []
bin_2 = []
bin_3 = []
bin_4 = []
bin_5 = []
bin_6 = []

for item in final_score:
    #HS
    if item[2] == 0:
        if item[1] < 0.33:
            bin_1.append(item[0])
        elif item[1] > 0.66:
            bin_3.append(item[0])
        else:
            bin_2.append(item[0])
    #NHS
    else:
        if item[1] < 0.33:
            bin_4.append(item[0])
        elif item[1] > 0.66:
            bin_6.append(item[0])
        else:
            bin_5.append(item[0])
        
print len(bin_1), len(bin_2), len(bin_3), len(bin_4), len(bin_5), len(bin_6)
