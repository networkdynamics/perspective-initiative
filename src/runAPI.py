#!/usr/bin/python
'''
Running the Perspective API
The function run_Perspective takes as input a string and returns the tocxicity score

@Saleem 
June 4, 2017
'''

#IMPORTS
import json
import os
import sys
from googleapiclient import discovery
import urllib2
from datetime import datetime
import time

#DATA SETTINGS
data_path = '../data/raw/'
file_name = sys.argv[1]
file_path = os.path.join(data_path, file_name)

with open(file_path, 'r') as fin:
    all_lines = fin.readlines()

#PERSPECTIVE SETTINGS
API_KEY='AIzaSyBMFtnhXjYR1iZhLUfywUbBahwxWLus6-c'
service = discovery.build('commentanalyzer', 'v1alpha1', developerKey=API_KEY)

def run_Perspective(comment):
    analyze_request = {
	'comment': { 'text': comment},
	'requestedAttributes': {'TOXICITY': {}}
    }
    response = service.comments().analyze(body=analyze_request).execute()
    return str(response['attributeScores']['TOXICITY']['summaryScore']['value'])

#RUNNING IT ALL
scores = []

counter = 0
total_counter = 0
a = datetime.now()
for line in all_lines:
    jobj = json.loads(line)
    text = jobj['body']
    text = ' '.join(text.split())
    if text != '[deleted]':
        try:
            scores.append(run_Perspective(text))
        except Exception, err:
            scores.append('ERROR: '+str(err)[1:-1].split('returned ')[-1][1:-1])
        counter += 1
        total_counter += 1
        if counter == 1000:
            print 1000
            b = datetime.now()
            print b-a
            tts = 100 - (b-a).seconds
            if tts > 0:
                print 'Sleeping', tts+5
                time.sleep(tts+5)
            counter = 0
            a = datetime.now()
            with open('API_'+file_name, 'a') as fout:
                for line in scores:
                    fout.write(line+'\n')
            scores = []
    if total_counter == 50000:
        break
with open('API_'+file_name, 'a') as fout:
    for line in scores:
        fout.write(line+'\n')
