import pandas as pd
import matplotlib as plt
import numpy as np

def rescore(weight_on_freq, aoa, freq):
    x = freq.multiply(weight_on_freq)
    return aoa + x

def flip_values(x):
    flipped = max(x)-x
    return flipped

def scale_between(x, minval, maxval):
    y = x-min(x)
    z = y.div(max(x))
    m = z.multiply((max(x))-([min(x)]))
    scaled = m + min(x)
    return scaled

def log_transform(x):
    log_trans = np.log10(x + 1)
    return log_trans

def log_transform_legacy(x):
    log_trans = np.log(x)
    return log_trans

mono_partial = pd.read_csv('mono_partial.csv')
weight_on_freq = 0.5
aoa = mono_partial['aoa']
freq = mono_partial['freq_lcnl']
mono_partial['score'] = rescore(weight_on_freq, aoa, freq)
mono_partial['freq_lcnl_log_flipscale'].corr(mono_partial['score'])
mono_partial['aoa_mean_scale'].corr(mono_partial['score'])

mono_scored = mono_partial[mono_partial.score.notnull()].sort_values(by ='score', ascending = True)
mono_scored.to_csv('mono_scored.csv', na_rep = '#N/A') 
sl = pd.read_excel("word-level_data/SUBTLEXusfrequencyabove1.xlsx")
ms= mono_scored.merge(sl, on = 'word', how = 'left')
ms_merge['log_value'] = np.log(ms_merge['FREQcount'])
print(ms_merge)