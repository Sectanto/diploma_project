#%%

import numpy as np
import pickle as pkl


with open('dataset0.pkl','rb') as f:
     data = pkl.load(f)
     print(data.shape)
#%%

import pandas as pd

columns = ['heading', 'authors', 'date_pub','url', 'article']
lim = 20000

df = pd.DataFrame({}, columns=columns)
for idx, row in enumerate(data):

    rows = row.split('.html')
    article = rows[-1]
    rows = ''.join(rows).split('--', 4)[1:]

    for idy, p in enumerate(rows):
        rows[idy] = p.strip("Z\n")

    if(len(rows) == 4):
        df.loc[len(df)] = rows + [article]
    if(idx== lim):
        break
df.set_index('date_pub', inplace=True)
df[:3]
#%%
# df.to_pickle('pandasArticles.pkl')
df.to_csv('pandasArticles.csv')
