
filenames = ['Personal_Pronoun_positive_features.txt', 'Personal_Pronoun_negative_features.txt']
with open('Merged_personal_pronoun_features.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)