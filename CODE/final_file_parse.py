
type_dict = {}
with open('Final_file.txt')as f:
	content = f.read()
	for line in content.split("\n"):
		if(line!=""):
			type_dict[line.split(",")[0]]=[]
with open('Final_file.txt')as f:
	content = f.read()
	for line in content.split("\n"):
		if(line!=""):
			predicted_label = int(line.split("::")[1])
			if(predicted_label==1):
				type_dict[line.split(",")[0]].append(line.split(",")[1]+':'+line.split(",")[2])

import glob, os
os.chdir('/home/user/git/CODE/GOLD_DEV_RESULTS')

gold_dict = {}

for file in glob.glob("*.ann"):
	gold_dict[file[:-4]]=[]
	content = open(file).read()
	for line in content.split("\n"):
		if(line!=""):
			if("Exp" in line.split("\t")[1]):
				gold_dict[file[:-4]].append(line.split(" ")[1] + "-" + line.split(" ")[2].split("\t")[0])


pred_dict={}
pred_dict_span ={}
os.chdir('/home/user/git/CODE')

with open('Final_file.txt')as f:
	content = f.read()
	for line in content.split("\n"):
		if(line!=""):
			pred_dict[line.split(",")[0]]=[]
			pred_dict_span[line.split(",")[0]]=[]

with open('Final_file.txt')as f:
	content = f.read()
	for line in content.split("\n"):
		if(line!=""):
			predicted_label = int(line.split("::")[1])
			if(predicted_label==1):
				pred_dict[line.split(",")[0]].append(line.split(",")[1])
				pred_dict[line.split(",")[0]].append(line.split(",")[2])
				pred_dict_span[line.split(",")[0]].append(line.split(",")[1] + ":" + line.split(",")[2])

def intersection(a, b):
    return list(set(a) & set(b))

def Average(lst):
	if(len(lst)>0):
		return(sum(lst) / len(lst))


## Mention Detection precision and recall
prec = []
rec = []

cont = 1
for file1 in gold_dict:
	for file2 in pred_dict:
		if(file1==file2):
			if(len(pred_dict[file2])>0 and len(gold_dict[file2])>0):
				p = float(len(intersection(pred_dict[file2], gold_dict[file1])))/float(len(pred_dict[file2]))
				r = float(len(intersection(pred_dict[file2], gold_dict[file1])))/float(len(gold_dict[file2]))
				prec.append(float(len(intersection(pred_dict[file2], gold_dict[file1])))/float(len(pred_dict[file2])))
				rec.append(float(len(intersection(pred_dict[file2], gold_dict[file1])))/float(len(gold_dict[file2])))
		

## Mention Referent Linking precision and recall

os.chdir('/home/user/git/CODE/GOLD_DEV_RESULTS')

ana_dict = {}
ant_dict = {}
for file in glob.glob("*.ann"):
	content = open(file).read()
	ana_dict[file] = []
	ant_dict[file] = []
	for line in content.split("\n"):
		if(line!=""):
			if(line.startswith("R")):
				anaphora = line.split("\t")[1].split(" ")[1].split(":")[1]
				antecedent = line.split("\t")[1].split(" ")[2].split(":")[1]
				
				for line1 in content.split("\n"):
					if(line1.startswith(anaphora)):
						#print(line1.split("\t")[1].split(" ")[1] + "-" + line1.split("\t")[1].split(" ")[2])
						ana_dict[file].append(line1.split("\t")[1].split(" ")[1] + "-" + line1.split("\t")[1].split(" ")[2])
					if(line1.startswith(antecedent)):
						#print(line1.split("\t")[1].split(" ")[1] + "-" + line1.split("\t")[1].split(" ")[2])
						ant_dict[file].append(line1.split("\t")[1].split(" ")[1] + "-" + line1.split("\t")[1].split(" ")[2])

gold_span_dict = {}

for file1 in ana_dict:
	for file2 in ant_dict:
		if(file1 == file2):
			gold_span_dict[file1]=[]
			list_of_spans_in_ana = ana_dict[file1]
			list_of_spans_in_ant = ant_dict[file2]
			
			for i in range(len(list_of_spans_in_ant)):
				gold_span_dict[file1].append(list_of_spans_in_ana[i] + ":" + list_of_spans_in_ant[i])

precision = []
recall = []
TP = []
FP = []
FN = []
for file1 in gold_span_dict:
	for file2 in pred_dict_span:
		if(file1[:-4] == file2):
			if(len(pred_dict_span[file2])>0 and len(gold_span_dict[file1])>0):
				#print(file2)
				for elem1 in pred_dict_span[file2]:
					for elem2 in gold_span_dict[file1]:
						if(elem1==elem2):
							TP.append(elem2)
						elif(elem1 not in gold_span_dict[file1]):
							FP.append(elem1)
						elif(elem2 not in pred_dict_span[file2]):
							FN.append(elem2)
							
				precision.append(float(len(intersection(pred_dict_span[file2], gold_span_dict[file1])))/float(len(pred_dict_span[file2])))
				recall.append(float(len(intersection(pred_dict_span[file2], gold_span_dict[file1])))/float(len(gold_span_dict[file1])))


for file2 in pred_dict_span:
	print(file2)
	print(pred_dict_span[file2])
	print(gold_span_dict[file2+'.ann'])

