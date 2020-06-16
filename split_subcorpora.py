# -*- coding: utf-8 -*-
"""
This script reads SpeakerIDs from the pickle outfile created by "speaker_metadata.py". Then it matches the SpeakersIDs
in outfile with those in a .csv file (cleanframe.csv) and writes a new csv. file that only contains the SpeakerIDs of
the pickle outfile.

See corpus annotation manual for complete tag list.

Created June 2020 at HK PolyU
@authors Andreas Liesenfeld and Gabor Parti
"""

import pandas as pd
import pickle

#input output paths
path = r'/home/andreas/Desktop/SpokenBNC/spoken/'
path_to_output = r'/home/andreas/Desktop/SpokenBNC/spoken/'

#read complete csv
df = pd.read_csv(path + 'cleanframe.csv', index_col=None, header=0)

## load pickle outline from speaker_metadata file
with open ('outfile', 'rb') as fp:
    selected_speakerIDs = pickle.load(fp)

##create empty df and fill with rows featuring selected speaker IDs, then save to disk
df2 = pd.DataFrame()
splitframe = df.query('(speaker in @selected_speakerIDs)').append(df2, ignore_index = True)
splitframe.to_csv(path_to_output + 'old_m.csv', index=False)
print(splitframe)

