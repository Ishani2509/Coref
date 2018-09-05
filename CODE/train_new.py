features_list = []
labels_list = []
int_features = []


with open('processed_final_feature_file.txt','w') as f:
	f1 = open('Final_feature_file.txt')
	content = f1.read()
	for line in content.split("\n"):
		if(not 'null' in line):
			f.write(line+'\n')

with open('processed_final_feature_file_dev.txt','w') as f2:
	f1 = open('Final_feature_file_dev.txt')
	content = f1.read()
	for line in content.split("\n"):
		if(not 'null' in line):
			f2.write(line+'\n')

with open('processed_final_feature_file.txt') as f:
	content = f.read()
	for line in content.split("\n"):
		if(line!=""):
			features = line.split("::")[0].split(",")[3:8]
			#print(features)
			int_feature=[]
			for elem in features:
				if(elem.isdigit()):
					int_feature.append(int(elem))
				else:
					int_feature.append(0)
			#print(int_feature)
			int_labels=[]
			labels = line.split("::")[1]
			for elem in labels:
				if(elem.isdigit()):
					int_labels.append(int(elem))
				else:
					int_labels.append(0)
				
			int_features.append(int_feature)
			labels_list.append(int_labels)


labels_list_dev = []
int_features_dev = []

with open('processed_final_feature_file_dev.txt') as f:
	content = f.read()
	for line in content.split("\n"):
		if(line!=""):
			features = line.split("::")[0].split(",")[3:8]
			int_feature=[]
			for elem in features:
				if(elem.isdigit()):
					int_feature.append(int(elem))
				else:
					int_feature.append(0)
			
			labels = line.split("::")[1]
			int_labels=[]
			for elem in labels:
				if(elem.isdigit()):
					int_labels.append(int(elem))
				else:
					int_labels.append(0)
				
			int_features_dev.append(int_feature)
			labels_list_dev.append(int_labels)


from sklearn import svm
from sklearn.metrics import confusion_matrix,precision_score,recall_score,f1_score
X = int_features
Y = labels_list

Xdev = int_features_dev
Ydev = labels_list_dev

clf = svm.SVC(kernel='linear')

clf.fit(X,Y)

ypred = clf.predict(Xdev)

output = open('Final_file.txt','w')
index = 0
for line in open('processed_final_feature_file_dev.txt').read().split("\n"):
	if(line!=""):
		output.write(line + "::" + str(list(ypred)[index]) + "\n")
	index = index + 1

print([i for i, e in enumerate(list(ypred)) if e == 1]	)
cm = confusion_matrix(Ydev, ypred)
print(cm)
tn, fp, fn, tp = cm.ravel()
print('TP = ' + str(tp))
print('TN = ' + str(tn))
print('FN = ' + str(fn))
print('FP = ' + str(fp))
print(precision_score(Ydev, ypred,average='macro'))
print(recall_score(Ydev, ypred,average='macro'))
print(f1_score(Ydev, ypred,	average='macro'))