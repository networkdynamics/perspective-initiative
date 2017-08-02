'''
Joining the results from Perspective and comment id.


@Saleem
June 6, 2017
'''

target = 'fatpeoplehate'

with open('scores_test_'+target+'.txt', 'r') as fin:
    all_scores = fin.readlines()

with open('test_'+target+'.txt', 'r') as fin:
    all_comms = fin.readlines()

import json

id_list = []
for item in all_comms:
    jobj = json.loads(item)
    id_list.append(jobj['id'])

for item in zip(id_list, all_scores):
    print item[0], item[1].strip()
