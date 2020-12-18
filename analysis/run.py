
# %%

directory_path = '20061020_20131126_bloomberg_news/'

from os import listdir
import codecs


subdirectory = {}
res_data = []
# earlyStop = input('earlyStop:')
# earlyStop = 1500

for f in listdir(directory_path):
    listDirectory = listdir(directory_path + f)
    subdirectory[f] = listDirectory
    
    for dirs in listDirectory:
        # earlyStop -= 1
        item = codecs.open(directory_path + f +'/'+ dirs, 'r', encoding='utf-8',
                 errors='ignore').read()
        res_data.append(item)

    # if(earlyStop <= 0):
        # break

# print(res[0].split('--'))
# %%
import pandas as pd

columns = ['heading', 'authors', 'date_pub','url', 'article']

data = pd.DataFrame({}, columns=columns)
for idx, row in enumerate(res_data):

    rows = row.split('.html')
    article = rows[-1]
    rows = ''.join(rows).split('--', 4)[1:]

    for idy, p in enumerate(rows):
        rows[idy] = p.strip("Z\n")

    if(len(rows) == 4):
        data.loc[len(data)] = rows + [article]

data.set_index('date_pub', inplace=True)
data

#%%

# date0 = pd.to_datetime("1, 1, 2009 23:0:0")
# data[date0:].to_csv('bloomberg_articles_data_2009-13', index=False)
data.to_csv('bloomberg_articles_data_2006-13')
#%%
x = data[date0:]
x.to_csv('bloomberg_articles_data_2009-13')

#%%
# data.to_pickle("pandas.pkl")
#%%
import numpy as np
import pickle as pkl

r = np.array(res_data, dtype=object)

# with open('data.pkl','wb') as f:
#     pkl.dump(r, f)
# %%
import numpy as np
x = np.array(['nice', 'one'], dtype=object)
x