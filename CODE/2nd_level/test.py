
file1 = open('Final_file.txt')
file2 = open('Final_file_test.txt')

lines1 = []
lines2 = []

for line in file1.read().split("\n"):
	if(line!=""):
		lines1.append(line.split("::")[2])

for line in file2.read().split("\n"):
	if(line!=""):
		lines2.append(line.split("::")[2])

li = []

for i in range(len(lines1)):
	if(lines1[i] == lines2[i]):
		li.append(True)

print(len(lines1))
print(len(li))


