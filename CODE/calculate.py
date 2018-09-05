
import matplotlib.pyplot as plt
f1 = open('tp_fp_actual.txt')

content = f1.read()
prec_list=[]
rec_list = []
for line in content.split("\n"):
	if(line!=""):
		tp = float(line.split(",")[0])
		fp = float(line.split(",")[1])
		fn = float(line.split(",")[2])
		if(tp!=0):
			prec = float(float(tp)/float(tp+fp))
			rec = float(float(tp)/float(tp+fn))
			#print(prec,rec)
			prec_list.append(prec)
			rec_list.append(rec)
		else:
			#print("(0.0, 0.0)")
			prec_list.append(float(0))
			rec_list.append(float(0))

print(float(sum(prec_list)/len(prec_list)))
print(float(sum(rec_list)/len(rec_list)))