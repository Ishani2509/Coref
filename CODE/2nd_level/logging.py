
## Mention Type index: corresponding Threshold
type_dict = {'DefiniteNP':'1;4', 'RelativePronoun':'2;1', 'PersonalPronoun':'3;4' , 
'PossessivePronoun':'4;5', 'DistributivePronoun':'5;4', 'DemonstrativeNP':'6;4', 
'DistributiveNP':'7;4', 'ReciprocalPronoun':'8;4'}

count = 0
lines = {}
with open('Final_Log.txt') as f:
	content = f.read()
	for line in content.split("\n"):
		if(line.startswith(" Processing file ")):
			count = count + 1
			filename = line.split(",")[1]
			lines[filename]={}

		if(line.startswith(" Scored Candidates for")):
			mention_type = line.split(";")[1]
			mention_span = line.split(";")[2]
			mention_index = type_dict[mention_type].split(";")[0]
			threshold = type_dict[mention_type].split(";")[1]
			candidates = line.split(";")[3].split(",")
			#print(mention_type + " " + mention_span)
			lines[filename][mention_type+":"+mention_span]={}
			list_of_cand_spans=[]
			scores = []
			for elem in candidates:
				names=elem.split("=")[0].split("|")[0].split("_")[-1][:-1]
				#print(names)
				try:
					score = elem.split("=")[1]
					if("}" in score):
						score = score.replace("}","")
					if(score.isdigit()):
						if(int(score)>=int(threshold)):
							isthreshold = 1
						if(int(score)==int(threshold)):
							istopscore = 1
						else:
							isthreshold = 0
							istopscore = 0
					else:
						isthreshold = 0
						istopscore = 0
				except IndexError:
					score = 'null'
					isthreshold = 0
				list_of_cand_spans.append(names+":"+score+":"+str(isthreshold)+":"+str(istopscore)+":"+mention_span+":"+type_dict[mention_type].split(";")[0])
			lines[filename][mention_type+":"+mention_span]['spans'] = list_of_cand_spans	
		
		if(line.startswith(" Best candidate with score")):
			score = line.split(":")[1]
			candidate = line.split(":")[2].split("_")[-1]	
			lines[filename][mention_type+":"+mention_span]['best'] = score+":"+candidate

filter_count = 0
filter_line = {}
best_line = {}
with open('Final_Log.txt') as f:
	content = f.read()
	for line in content.split("\n"):
		if(line.startswith(" Processing file ")):
			filter_count = filter_count + 1
			filename = line.split(",")[1]
			filter_line[filename]={}
			best_line[filename]={}
		if(line.startswith(" Scored Candidates for")):
			mention_span = line.split(";")[2]
			mention_type = line.split(";")[1]
			filter_line[filename][mention_type+":"+mention_span]=[]
			best_line[filename][mention_type+":"+mention_span]=[]
		if(" Passed Filter 3" in line):
			target_cand = line.split(" ")[1]
			filter_line[filename][mention_type+":"+mention_span].append(target_cand)
		if(" Best candidate " in line):
			score = line.split(":")[1]
			cand = line.split(":")[2]
			if(cand.isdigit()):
				best_line[filename][mention_type+":"+mention_span].append(cand)
			else:
				best_line[filename][mention_type+":"+mention_span].append(cand.split("_")[-1][:-1])
write_file = open('Write_output.txt','w')

for file1 in filter_line:
	for file2 in lines:
		if(file2==file1):
			#write_file.write(file1+'\n')
			for elem1 in list(filter_line[file1].keys()):
				for elem2 in list(lines[file2].keys()):
					if(elem1==elem2):
						#write_file.write(elem1+'\n')
						#print(elem2, filter_line[file1][elem1], lines[file1][elem1])
						if(len(filter_line[file1][elem1])==0):
							for elem in lines[file1][elem1]['spans']:
								write_file.write(elem+":"+'0'+ ','+file1 +'\n')
						else:
							filt_cand = str(filter_line[file1][elem1])[2:-2]
							#write_file.write('Filter =' + filt_cand+'\n')
							for elem in lines[file1][elem1]['spans']:
								if(elem.split(":")[0]==filt_cand):
									write_file.write(elem + ":" + '1'+ ','+ file1 +'\n')
								else:
									write_file.write(elem + ":" + '0'+ ','+file1 +'\n')
							

best = open('best_file','w')
for file in lines:
	for elem in lines[file]:
		spans = lines[file][elem]['spans']
		best_span = lines[file][elem]['best'].split(":")[1]
		if(")" in best_span):
			best_span = best_span.replace(")","")
		#print(spans, best_span)
		for elem in spans:
			mention_span = elem.split(":")[0]
			if(best_span == mention_span):
				best.write(elem + "::1"+'\n')
			else:
				best.write(elem + "::0"+'\n')

write_content = open('Write_output.txt')
best_content = open('best_file')

combine =[]

with open("Write_output.txt") as xh:
  with open('best_file') as yh:
    with open("feature_file","w") as zh:
      #Read first file
      xlines = xh.readlines()
      #Read second file
      ylines = yh.readlines()
      #Combine content of both lists  and Write to third file
      for line1, line2 in zip(xlines, ylines):
        zh.write("{} \t {}\n".format(line1.rstrip(), line2.rstrip()))