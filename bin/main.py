import pandas as pd
import numpy as np
from parse import render
from exporter import upload
from scrapy import scrapeData

import os

def process(url):
    
    extension = '.html'
    filename = url.split('/')[-2] + extension

    htmlres = render(url)

    file = open(filename, 'w', encoding="utf-8")
    file.write(htmlres)
    file.close()

    scrapeData('/home/zssvaid/workdir/'+filename)
    
    
    if(upload(filename)):
        os.remove("datasets/" + filename)


if(__name__ == "__main__"):
    dataset = pd.read_csv('data')
    for url in dataset['loc'].values:
        process(url)