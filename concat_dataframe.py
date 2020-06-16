# -*- coding: utf-8 -*-
"""
This script concatenates .csv files into one file ("oneframe.csv").
Built for SpokenBNC corpus data (http://corpora.lancs.ac.uk/bnc2014/).
See corpus annotation manual for complete tag list.

Created June 2020 at HK PolyU
@authors Andreas Liesenfeld and Gabor Parti
"""


import pandas as pd
import glob

path = r'/home/andreas/Desktop/SpokenBNC/spoken/csv_complete'
path_to_output = r'/home/andreas/Desktop/SpokenBNC/spoken/'

all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

frame.to_csv(path_to_output + 'oneframe.csv', index=False)

print(frame)