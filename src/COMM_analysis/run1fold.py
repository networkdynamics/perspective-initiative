# voat
# python mainModule.py reddit onefold svm coontown opprandom voat coontown random
import os

themes = ['coontown', 'fatpeoplehate', 'theredpill']
algos = ['lr']


for theme in themes:
    for algo in algos:
        cmd = ' '.join(['python', 'mainModule.py', 'reddit', 'onefold',
                        algo, theme, 'opprandom', 'voat', theme, 'random'])
        os.system(cmd)
