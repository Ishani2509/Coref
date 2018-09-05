
f1 = open('Dev.txt')
content = f1.read()

count = 1
lines={}
for line in content.split("\n"):
	if(line!=""):
		lines["qid:"+str(count)]=[]
		if("qid:"+str(count) in line):
			print(line)
			lines["qid:"+str(count)].append(line)
count=count+1

print(lines)