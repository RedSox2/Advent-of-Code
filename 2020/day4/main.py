from sys import argv
import regex as re
with open(f'{argv[1]}.txt', 'r') as file: 
	passports = file.read().strip().split('\n\n')
	req = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']

	# part 1

	valid = 0
	for i in passports: 
		if all(n in i for n in req): 
			valid += 1
	print(valid)

	# part 2
	valid = 0
	passports = [i.split() for i in passports]
	for i in passports: 
		r = []
		for n in req: 
			r.append(any(n in j for j in i))
		if not all(r): 
			continue

		for n in i: 
			if 'byr:' in n: 
				if not 1920 <= int(n[4:]) <= 2002: 
					break	
			elif 'iyr:' in n: 
				if not 2010 <= int(n[4:]) <= 2020: 
					break
			elif 'eyr:' in n: 
				if not 2020 <= int(n[4:]) <= 2030: 
					break
			elif 'hgt:' in n: 
				if n[-2:] == 'cm': 
					if not 150 <= int(n[4:-2]) <= 193: 
						break
				elif n[-2:] == 'in': 
					if not 59 <= int(n[4:-2]) <= 76:
						break
				else: 
					break
			elif 'hcl:' in n: 
				if not re.search('#[0-9a-f]{6}', n): 
					break
			elif 'ecl:' in n: 
				if n[4:] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: 
					break
			elif 'pid:' in n: 
				if not (len(n[4:]) == 9 and n[4:].isdigit()): 
					break
		else: 
			valid += 1
			print('valid')
			print(i)
			print('')
	print(f'Valid: {valid}')		

