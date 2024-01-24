import re

file = open('dataset', 'r')
fileContent = file.read()
file.close()

times = re.findall(r'[A-Z],\d+,\d+', fileContent)

file = open('parsed', 'w')
for i in times:
	data = i.split(',')	
	file.write(data[2] + '\n')
file.close()
