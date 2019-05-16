import pandas as pd
words= pd.read_csv('3k/words.csv', header=None, keep_default_na = False)
phon= pd.read_csv('3k/phon.csv', header=None)
orth= pd.read_csv('3k/orth.csv', header=None)
#words[words[0].isnull()] = 'null'

phon = phon.set_index(word[0])
orth = orth.set_index(word[0])
phon.loc[['fawn','hitch']]

mono = pd.read_csv ('mono_partial1000.csv')
print(mono.shape)
mono = mono[mono['source'] == '3k']
print(mono.shape)
aoa = mono['word'][0:300]
#print (aoa)

x = [0]*2881
y = [0]*2881

for i in range(2881):
    x[i] = any(aoa.eq(word[0][i]))
    y[i] = not x[i]
    
sum(x)

#opwords = pd.read_csv("3k/opwords.csv")
#training = opwords[opwords["value"] == "training"]
#training_set = training[["words"]]
training_set = pd.Series(words[x][0])
testing_set = pd.Series(words[y][0])

orth.loc[training_set].to_csv("3k/orth_aoa300_reps_train.csv", header=False)
orth.loc[testing_set].to_csv("3k/orth_aoa300_reps_test.csv", header=False)
phon.loc[training_set].to_csv("3k/phon_aoa300_reps_train.csv", header=False)
phon.loc[testing_set].to_csv("3k/phon_aoa300_reps_test.csv", header=False)
mono_scored_extended = pd.read_csv("mono_scored_extended.csv", header = 0, keep_default_na=False)