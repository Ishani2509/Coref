
f1 = open('Final_feature_file_dev.txt','w')

with open('feature_file')as f:
	content = f.read()
	for line in content.split("\n"):
		if(line!=""):
			try:
				first = line.split("\t")[0]
				second = line.split("\t")[1]
				file = first.split(",")[1]
				cand = first.split(",")[0].split(":")[0]
				mention = first.split(",")[0].split(":")[4]
				score = first.split(",")[0].split(":")[1]
				isthreshold = first.split(",")[0].split(":")[2]
				istopscore = first.split(",")[0].split(":")[3]
				isfilter = first.split(",")[0].split(":")[6]
				mention_type = first.split(",")[0].split(":")[5]
				#isprotein = first.split(",")[0].split(":")[7]
				label = second.split("::")[1]
				f1.write(file[:-1]+','+mention+','+cand+','+mention_type+','+score+','+isthreshold+','+istopscore+','+isfilter +'::'+label+'\n')
			except:
				pass

