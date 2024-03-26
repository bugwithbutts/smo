import re

file = open('raw_data/prob_test_data', 'r', encoding='utf-8')
fileContent = file.read()
file.close()

# times = re.findall(r'[A-Z],\d+,\d+', fileContent)
tests = re.findall(r'[A-Z]-.+\d\d\d\.cpp', fileContent)

# file = open('parsed_s22', 'w')
# for i in times:
# 	data = i.split(',')	
# 	file.write(data[2] + '\n')
# file.close()

file = open('parsed_data/parsed_ptz', 'w')
for i in tests:
	data = i.split('-')
	file.write(data[0] + ' ' + data[5][:3] + '\n')
file.close()