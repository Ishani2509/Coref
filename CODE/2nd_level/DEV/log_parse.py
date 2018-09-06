import glob, os
final_log = open('Final_Log.txt','w')
with open('logs.txt')as f:
	content = f.read()
	line_count = 1
	for line in content.split("\n"):
		if(line_count%2 == 0):
			final_log.write(line[5:]+'\n')
		line_count = line_count + 1

