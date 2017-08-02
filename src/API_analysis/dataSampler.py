'''
Data Sampler
Get Reddit comments with socres less than and greater than some value.

@Saleem
June 4, 2017
'''

#IMPORTS
import json
import sys
import os

#DATA SETTINGS
data_path = '../data/'
file_name = sys.argv[1]
file_path = os.path.join(data_path, file_name)

with open(file_path, 'r') as fin:
    all_lines = fin.readlines()

p_count = 0
n_count = 0

p_file = os.path.join(data_path, 'pos_sample_'+file_name)
n_file = os.path.join(data_path, 'neg_sample_'+file_name)

#RUNNING IT ALL
with open(p_file, 'w') as p_out:
    with open(n_file, 'w') as n_out:
        for line in all_lines:
            jobj = json.loads(line)
            if jobj['score'] < -100:
                if jobj['body'] != '[deleted]':
                    if n_count < 100:
                        n_out.write(line)
                        n_count +=1
            if jobj['score'] > 100:
                if jobj['body'] != '[deleted]':
                    if p_count < 100:
                        p_out.write(line)
                        p_count +=1
            if p_count == 100 and n_count == 100:
                break
