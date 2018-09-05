final_dict = {}
with open('Final_feature_file_train.txt')as f:
	content= f.read()
	for line in content.split("\n"):
		if(line!=""):
			filename = line.split(",")[0]
			mention = line.split(",")[1]
			final_dict[filename+","+mention]={}
			if(line.startswith(filename+","+mention)):
				final_dict[filename+","+mention]['spans']=[]
				final_dict[filename+","+mention]['features']=[]
				final_dict[filename+","+mention]['labels']=[]
				for line1 in content.split("\n"):
					if(line1.startswith(filename+","+mention)):
						final_dict[filename+","+mention]['spans'].append(line1.split(",")[2])
						final_dict[filename+","+mention]['features'].append(line1.split(",")[3:9])
						final_dict[filename+","+mention]['labels'].append(line1.split("::")[1])

write_file=open('train_data.txt','w')
list_of_files = list(final_dict.keys())
dictionary_of_files={}

for i in range(len(list_of_files)):
	dictionary_of_files[list_of_files[i]]=i+1

print(dictionary_of_files)
for file in final_dict:
	labels = final_dict[file]['labels']
	spans = final_dict[file]['spans']
	features = final_dict[file]['features']
	int_features = []
	for feature in features:
		int_feature=[]
		i = 1
		for elem in feature:
			if("::" in elem):
				elem = elem.replace("::","")[:-1]
				int_feature.append(str(i) +":" + elem)
			else:
				elem = elem
				int_feature.append(str(i) +":" + elem)
			i=i+1
		int_features.append(int_feature)

	length = len(int_features)

	for i in range(length):
		write_file.write(str(labels[i]) + " " + "qid:"+str(dictionary_of_files[file]) + " " + str(int_features[i])[1:-1] +'\n')

read_file = open('train_data.txt')
final_train_file = open('Dev.txt','w')
for line in read_file.read().split("\n"):
	if("," in line):
		line = line.replace(",","")
	if("'" in line):
		line = line.replace("'","")
	final_train_file.write(line+'\n')