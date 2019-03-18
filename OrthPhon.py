import pandas as pd
words= pd.read_csv('3k/words.csv', header=None, keep_default_na = False)
phon= pd.read_csv('3k/phon.csv', header=None)
orth= pd.read_csv('3k/orth.csv', header=None)
phon = phon.set_index(words[0])
orth = orth.set_index(words[0])
mono = pd.read_csv ('mono_partial1000.csv')
mono = mono[mono['source'] == '3k']
aoa = mono['word'][0:300]
#print (aoa)"
x = [0]*2881
y = [0]*2881
for i in range(2881):
    x[i] = any(aoa.eq(words[0][i]))
    y[i] = not x[i]
    
sum(x)
#opwords = pd.read_csv("3k/opwords.csv")
#training = opwords[opwords["value"] == "training"]
#training_set = training[["words"]]
training_set = pd.Series(words[x][0])
testing_set = pd.Series(words[y][0])
orthaoa300testing = pd.DataFrame(testing_set)
orthaoa300testing.to_csv ("3k/orthaoa300testing.csv")
orthaoa300training = pd.DataFrame (training_set)
orthaoa300training.to_csv ("3k/orthaoa300training.csv")
phonaoa300training = pd.DataFrame (training_set)
phonaoa300training.to_csv ("3k/phonaoa300training.csv")
phonaoa300testing = pd.DataFrame (testing_set)
phonaoa300testing.to_csv ("3k/phonaoa300testing.csv")
orth.loc[training_set].to_csv("3k/orth_aoa300_reps_train.csv", header=False)
orth.loc[testing_set].to_csv("3k/orth_aoa300_reps_test.csv", header=False)
phon.loc[training_set].to_csv("3k/phon_aoa300_reps_train.csv", header=False)
phon.loc[testing_set].to_csv("3k/phon_aoa300_reps_test.csv", header=False)

