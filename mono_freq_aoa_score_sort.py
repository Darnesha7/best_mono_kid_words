import pandas as pd
import matplotlib as plt
import numpy as np

def rescore(d,weight_on_freq):
    wf = weight_on_freq
    wa = 1 #weight on aoa
    x = d['freq_lcnl_log_flipscale'].multiply(weight_on_freq)
    return d['aoa_mean_scale'] + x

mono_partial= pd.read_csv('mono_partial.csv')

mono_partial['score'] = rescore(mono_partial,0.5)
mono_partial['freq_lcnl_log_flipscale'].corr(mono_partial['score'])
mono_partial['aoa_mean_scale'].corr(mono_partial['score'])

mono_scored = mono_partial[mono_partial.score.notnull()].sort_values(by ='score', ascending = True)
#mono_scored.to_csv('mono_scored.csv', na_rep = '#N/A')
ms = mono_scored[mono_scored["freq_lcnl_log"] > 0]
print (ms)
min(ms["freq_lcnl_log"])
sl = pd.read_excel("word-level_data/SUBTLEXusfrequencyabove1.xlsx")
mono_scored_merge = mono_scored.merge(sl, on = 'word', how = 'left')
mono_scored_merge['log_value'] = np.log(mono_scored_merge['FREQcount'])
print(mono_scored_merge)
