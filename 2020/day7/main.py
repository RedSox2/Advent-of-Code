from sys import argv
import regex as re
with open(f'{argv[1]}.txt', 'r') as file: 
	rules = file.read().strip().split('\n')
	
	bags = []

	for r in rules: 
		r = re.split(' bags contain [0-9] '
	
