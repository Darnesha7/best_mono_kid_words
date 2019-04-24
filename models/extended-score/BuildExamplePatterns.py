import pandas as pd

# Load wordlist with word level statistics
d = pd.read_csv("data/mono_scored_extended.csv", header = 0, keep_default_na=False)

# Load pre-constructed orth and phon representations
words= pd.read_csv('data/3k/words.csv', header=None, keep_default_na = False).iloc[:,0]
phon= pd.read_csv('data/3k/phon.csv', header=None)
orth= pd.read_csv('data/3k/orth.csv', header=None)

phon = phon.set_index(words)
orth = orth.set_index(words)

# Filter to sources of interest
z = d['source'] == '3k'
d = d.loc[z,:]

# Filter rows with missing data on variables of interest
z = d['score_extended'].notnull()
d = d.loc[z,:]

# Sort on dimensions of interest
d = d.sort_values(by ='score_extended', ascending = True)

# Select training and test sets
train_words = d['word'][0:300]
test_words = d['word'][300:]

# Pair with Orth and Phon patterns
train_orth = orth.loc[train_words,:]
train_phon = phon.loc[train_words,:]
test_orth = orth.loc[test_words,:]
test_phon = phon.loc[test_words,:]

# Write example files
train_phon.to_csv('train_orth.csv')
train_phon.to_csv('train_phon.csv')
test_orth.to_csv('test_phon.csv')
test_phon.to_csv('test_orth.csv')