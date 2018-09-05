
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
			predicted_label = int(line.split("::")[2])
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
			predicted_label = int(line.split("::")[2])
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
for file1 in gold_span_dict:
	for file2 in pred_dict_span:
		if(file1[:-4] == file2):
			if(len(pred_dict_span[file2])>0 and len(gold_span_dict[file1])>0):
				precision.append(float(len(intersection(pred_dict_span[file2], gold_span_dict[file1])))/float(len(pred_dict_span[file2])))
				recall.append(float(len(intersection(pred_dict_span[file2], gold_span_dict[file1])))/float(len(gold_span_dict[file1])))

os.chdir('/home/user/git/CODE')
write_file = open('Sentence_window_statistics.txt','w')

os.chdir('/home/user/git/Datasets/BIONLP/XML_FULL')
import xml.etree.ElementTree as ET

XML_dict_span = {}

for file in glob.glob("*.xml"):
	tree = ET.parse(file)
	fileid = tree.getroot().attrib['id']
	root = tree.getroot()
	XML_dict_span[fileid] = []
	for child in root:
		if(child.tag == 'sentence'):
			XML_dict_span[fileid].append(child.attrib['id']+":"+child.attrib['charOffset'])

#print(XML_dict_span)


for file1 in gold_span_dict:
	for file2 in XML_dict_span:
		if(file2 == file1[:-4]):
			#print(file2)
			coref_elements = gold_span_dict[file1]
			xml_sentences = XML_dict_span[file2]
			for elem in coref_elements:
				span_elem1 = elem.split(":")[0]
				span_elem2 = elem.split(":")[1]
				#print(span_elem2, span_elem1)
				sent1 = 0
				sent2 = 0
				for item in xml_sentences:
					span2_beg = span_elem2.split("-")[0]
					span2_end = span_elem2.split("-")[1]
					span1_beg = span_elem1.split("-")[0]
					span1_end = span_elem1.split("-")[1]

					span = item.split(":")[1]
					sp_beg = span.split("-")[0]
					sp_end = span.split("-")[1]
					#print(span2_beg, span2_end, sp_beg, sp_end)
					
					if(int(span2_beg)>=int(sp_beg) and (int(span2_end)<=int(sp_end))):
						sent1=int(item.split(":")[0][-1])
					if(int(span1_beg)>=int(sp_beg) and (int(span1_end)<=int(sp_end))):
						sent2=int(item.split(":")[0][-1])

				write_file.write(span_elem2+","+span_elem1+":"+str(abs(sent1-sent2))+'\n')

os.chdir('/home/user/git/CODE')
open_file = open('Sentence_window_statistics.txt')

content = open_file.read()

sentence_window = []
for line in content.split("\n"):
	if(line!=""):
		sentence_window.append(line.split(":")[1])

print(max(sentence_window))
print(min(sentence_window))

window_set = set(sentence_window)
print(window_set)

elements = []
val_elements = []
for elem in window_set:
	elements.append(int(elem))	
	val_elements.append(int(sentence_window.count(elem))*3)
	print(str(elem)+ "," + str(sentence_window.count(elem)*3))


import matplotlib.pyplot as plt
plt.bar(elements, val_elements)
plt.axis([0,9, 0, 1200])
plt.xlabel('Sentence Window')
plt.ylabel('Number of corefering pairs')
plt.title('Sentence Window vs Number of corefering pairs')
plt.show()