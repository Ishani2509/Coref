
Input File : logs.txt

Parse the log file :
	python log_parse.py >> Convert the logs.txt to Final_Log.txt : Final output of the log file which will contain the necessary lines to parse.

Finally convert the Final_log.txt to feature_file.txt :
	python logging.py ( intermediate output : Write_output.txt, best_file)

Run : python feature_extraction.py
	Convert into Final_feature_file.txt

Compare : the predicted vs actual rule-based precision and recall:
	Run python train_new.py

Create the Final_file.txt
PMID-10089566,390-401,15-32,6,1,0,0,0::0::0
PMID-10089566,390-401,305-319,6,1,0,0,0::0::0
PMID-10089566,390-401,0-11,6,1,0,0,0::0::0
PMID-10089566,390-401,232-256,6,1,0,0,0::0::0
PMID-10089566,390-401,260-292,6,1,0,0,0::0::0
PMID-10089566,390-401,52-62,6,1,0,0,0::0::0

Predicts: How many TP, FP, FN generated compared to the output of the Bioscores model.
	-- Using Linear SVM, the F-score of compared results = 96%.
	-- Accuracy 99%

Then run : python final_file_parse.py
	Compares the output of the gold standard and checks the performance after training the output.

	Mention Detection : 
	0.766310541311
	0.530595477089

	Mention Referent Linking:
	0.626638176638
	0.422883597884

This will provide us with the exact match.
In order to check how many exact matches are present in the data.
	-- We prepare manually tp_fp_actual.txt(from final_file_parse.py:: Change the predicted_label[1] to [2])
	-- We prepare manually tp_fp_pred.txt(from final_file_parse.py:: Change the predicted_label[1] to [2])
	-- python calculate.py
	(Print the prec, recall finally)
	
	Results:
	P = 0.740573372206
	R = 0.650013497462
