
						Logs generated from the Java path
								>> logs.txt

***Parse the log_files and divide the logs according to different categories:
	>> Input: logs.txt
	>> Run : log_parse_file.py
	>> Output: 'RelativePronounfile.txt', 'DemonstrativePronounfile.txt', 'DistributivePronounfile.txt', 'PersonalPronounfile.txt', 'PossessivePronounfile.txt', 'DefiniteNPfile.txt', 'InDefiniteNPfile.txt', 'DistributiveNPfile.txt', 'DemonstrativeNPfile.txt'

***For each of the categories perform feature extraction: 
(For example: Personal Pronoun)
	>> Input: 'PersonalPronounfile.txt'
	>> Run: Personal_pronoun_Feature_extraction.py
	>> Output: 'Personal_Pronoun_features.txt'

***For all the categories perform a combined feature vector generation:
	>> Input: dictionary = {'Personal_Pronoun_features.txt':4, 'Possessive_Pronoun_features.txt':5, 'Distributive_Pronoun_Positive_features.txt':2,
	'Relative_Pronoun_Positive_features.txt':1,  'Definite_NP_Positive_features.txt':2, 'Distributive_NP_Positive_features.txt':2, 'Demonstrative_NP_Positive_features.txt':2}

	>> Run : Feature_vector_generation.py
	>> Output: write_Personal_Pronoun_features.txt, write_other_infoPersonal_Pronoun_features.txt, merge_Personal_Pronoun_features.txt and so on... 

***For all the categories append the training labels to the categories:
	>> Input: 'merge_Personal_Pronoun_features.txt', 'merge_Possessive_Pronoun_features.txt' and so on..
	>> Run: create_training_label.py
	>> Output: Output_file.txt

***Divide the feature_vectors into different categories:(Personal Pronoun, Possessive pronoun, Relative pronoun, Definite NP, Indefinite NP, Demonstrative Pronoun, Distributive Pronoun, Distributive NP):

	>> Input: Output_file.txt
	>> Run: divide_feature_vectors.py
	>> Output: Feature_vectors_Relative_Pronoun, Feature_vectors_Personal_Pronoun, Feature_vectors_Possessive_Pronoun, etc.	

*** Train the model using the feature vectors of all the categories:

	>>> Input: Feature_vectors_Relative_Pronoun
	>>> Run : python train.py
	>>> Output: 