import os

themes = ['theredpill', 'coontown', 'fatpeoplehate']
algos = ['lr']


for theme in themes:
	for algo in algos:
		cmd = ' '.join(['python', 'mainModule.py', 'reddit', '10fold', algo, theme, 'random'])
		os.system(cmd)

