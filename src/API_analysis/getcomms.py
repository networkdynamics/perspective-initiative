import json
import sys

bins = sys.argv[1]

with open(bins, 'r') as fin:
    all_comms = fin.readlines()

all_comms = set([x.strip() for x in all_comms])

datafile = '/home/ndg/users/hsalee/perspective-initiative/data/coontown.txt'

with open(datafile, 'r') as fin:
    all_lines = fin.readlines()

for line in all_lines:
    jobj = json.loads(line)
    j_id = jobj['id']
    if j_id in all_comms:
        try:
            print ' '.join(jobj['body'].split())
        except UnicodeEncodeError:
            continue
