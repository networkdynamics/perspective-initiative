import operator
from collections import Counter
import os


data_path = '/home/ndg/users/hsalee/dangerous-speech/work/community_driven_hatespeech/datacollection/jigsaw/'
textfile = 'toxicity_annotated_comments.tsv'

filepath1 = os.path.join(data_path, textfile)

with open(filepath1, 'r') as fin:
    lines = fin.readlines()

data = {}


def betterprint(line):
    record = {}
    line = line.strip().split('\t')
    l_id = int(float(line[0]))
    text = line[1].replace("NEWLINE_TOKEN", " ")
    text = text.replace("`", " ")
    text = text.replace("=", " ")
    text = text.replace(":", " ")
    text = text.strip()
    text = " ".join(text.split())
    record['text'] = text
    record['score'] = 0
    data[l_id] = record
    return


for line in lines[1:]:
    betterprint(line)


annfile = 'toxicity_annotations.tsv'
filepath2 = os.path.join(data_path, annfile)

with open(filepath2, 'r') as fin:
    lines = fin.readlines()

data_label = {}

for line in lines[1:]:
    line = line.strip().split('\t')
    l_id = int(float(line[0]))
    tox = int(line[2])
    if l_id not in data_label:
        data_label[l_id] = []
    data_label[l_id].append(tox)

counter = 0

for item in data_label:
    record = Counter(data_label[item])
    tox = record.most_common(1)[0][0]
    data[item]['score'] = tox
    counter += tox

print counter
