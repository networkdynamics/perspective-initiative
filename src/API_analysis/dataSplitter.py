'''
Data Splitter
Create test and training sample

@Saleem
June 4, 2017
'''

#IMPORTS
import json
import sys
import os
import random
random.seed(21)

#DATA SETTINGS
data_path = '../data/'
out_path = '../data/classifier/'
file_name = sys.argv[1]
file_path = os.path.join(data_path, file_name)
random_path = os.path.join(data_path, 'random.txt')

with open(file_path, 'r') as fin:
    all_lines = fin.readlines()

text_lines = []
for line in all_lines:
    jobj = json.loads(line)
    if jobj['body'] != '[deleted]':
        #if len(jobj['body'].split()) > 20:
        text_lines.append(line)
random.shuffle(text_lines)
text_len = len(text_lines)
if text_len > 250000:
    text_lines = text_lines[:250000]
text_len = len(text_lines)


with open(file_path, 'r') as fin:
    all_lines = fin.readlines()

random_lines = []
for line in all_lines:
    jobj = json.loads(line)
    if jobj['body'] != '[deleted]':
        #if len(jobj['body'].split()) > 20:
        random_lines.append(line)
random.shuffle(random_lines)
random_lines = random_lines[:text_len]

#DATA SPLITTING
train_len = text_len * 4 / 5

train_text = text_lines[:train_len]
test_text  = text_lines[train_len:]

train_random = random_lines[:train_len]
test_random  = random_lines[train_len:]

#WRITING FILES
tr_file = os.path.join(out_path, 'train_'+file_name)
with open(tr_file, 'w') as fout:
    for line in train_text:
        fout.write(line)

tt_file = os.path.join(out_path, 'test_'+file_name)
with open(tt_file, 'w') as fout:
    for line in test_text:
        fout.write(line)

tr_file = os.path.join(out_path, 'train_random_'+file_name)
with open(tr_file, 'w') as fout:
    for line in train_random:
        fout.write(line)

tt_file = os.path.join(out_path, 'test_random_'+file_name)
with open(tt_file, 'w') as fout:
    for line in test_random:
        fout.write(line)
