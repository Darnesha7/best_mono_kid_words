import pandas as pd
import matplotlib as plt
import numpy as np
import math

def rescore(weight_on_freq):
    wf = weight_on_freq
    wa = 1 #weight on aoa
    x = ['freq_lcnl_log_flipscale'].multiply(weight_on_freq)
    return d['aoa_mean_scale'] + x

def flip_values(x):
    flip_values = max(x)-x
    return flipped

def scale_between(x, minval, maxval):
    y = x- min(x)
    z = y.div(max(x))
    m = z.multiply((max(x))-([min(x)])
    a = m + min(x)
    return scaled

def log_transform(x):
    freq_lcnl_log = math.log10(freq_lcnl)
    log_trans = log(x + 1)
    return log_trans
mono_partial = pd.read_csv('mono_partial.csv')

xlrd >= 1.0
mono_partial['score'] = rescore(mono_partial,0.5)
mono_partial['freq_lcnl_log_flipscale'].corr(mono_partial['score'])
mono_partial['aoa_mean_scale'].corr(mono_partial['score'])

mono_scored = mono_partial[mono_partial.score.notnull()].sort_values(by ='score', ascending = True)
new_mono_scored.to_csv('new_mono_scored.csv', na_rep = '#N/A') 
sl = pd.read_excel("word-level_data/SUBTLEXusfrequencyabove1.xlsx")
new_ms= m.merge(sl, on = 'word', how = 'left')
new_ms_merge['log_value'] = np.log(new_ms_merge['FREQcount'])
print(new_ms_merge)