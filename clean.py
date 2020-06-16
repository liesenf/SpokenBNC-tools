# -*- coding: utf-8 -*-
"""
This script reads SpokenBNC .csv files and removes and replaces various xml elements and tags
using replace and regex operations. Then it writes a .csv file back and tests for
">" in the new file.
Built for SpokenBNC corpus data (http://corpora.lancs.ac.uk/bnc2014/).
See corpus annotation manual for complete tag list.

Created June 2020 at HK PolyU
@authors Andreas Liesenfeld and Gabor Parti
"""

import pandas as pd
import re

path = r'/home/andreas/Desktop/SpokenBNC/spoken/'
path_to_output = r'/home/andreas/Desktop/SpokenBNC/spoken/'

# # Change filename here to load testframe small or big
df = pd.read_csv(path + 'oneframe.csv', index_col=None, header=0)

# # list with patterns that are deleted
To_remove_lst = ["</u>", "<unclear>", "</unclear>"]
To_change_short_pause = ["<pause dur=\"short\" />"]
To_change_long_pause = ["<pause dur=\"long\" />"]
To_change_unclearutt = ["<unclear />"]
To_change_startsinging = ["<shift new=\"singing\" />"]
To_change_endsinging = ["<shift new=\"normal\" />"]
To_change_truncbegin = ["<trunc>"]
To_change_truncend = ["</trunc>"]

#find pattern from list above and remove it
df['utterance'] = df['utterance'].str.replace('|'.join(To_remove_lst), '')
df['utterance'] = df['utterance'].str.replace('|'.join(To_change_short_pause), 'pauseshort')
df['utterance'] = df['utterance'].str.replace('|'.join(To_change_long_pause), 'pauselong')
df['utterance'] = df['utterance'].str.replace('|'.join(To_change_unclearutt), 'unclearutt')
df['utterance'] = df['utterance'].str.replace('|'.join(To_change_startsinging), 'startsinging')
df['utterance'] = df['utterance'].str.replace('|'.join(To_change_endsinging), 'endsinging')
df['utterance'] = df['utterance'].str.replace('|'.join(To_change_truncbegin), 'truncstart ')
df['utterance'] = df['utterance'].str.replace('|'.join(To_change_truncend), ' truncend')

# re.sub to remove eveything up to first occurance of ">"
df['utterance'] = [re.sub("^.*?>", "", str(x)) for x in df['utterance']]

# re.sub with custom function to subsitute "event desc" with event+description of event in one word
def my_replace_for_event(match):
    match = match.group()
    return re.sub("\W|desc", "", str(match))

df['utterance'] = [re.sub("<event desc=\"(\w*(\s?\w*)*\")\s\/>", my_replace_for_event, str(x)) for x in df['utterance']]

# re.sub with custom function to subsitute "vocal desc" with vocal+description of vocal in one word
def my_replace_for_vocal(match):
    match = match.group()
    return re.sub("\W|desc", "", str(match))

df['utterance'] = [re.sub("<vocal desc=\"(\w*(\s?\w*)*\")\s\/>", my_replace_for_vocal, str(x)) for x in df['utterance']]

# re.sub with custom function to delete the foreign language tags, but keep the foreign words and sentences
def my_replace_for_foreignstart(match):
    match = match.group()
    return re.sub("\<foreign\slang=\"\w\w\w\"\>", "", str(match))
df['utterance'] = [re.sub("\<foreign\slang=\"\w\w\w\"\>", my_replace_for_foreignstart, str(x)) for x in df['utterance']]

def my_replace_for_foreignend(match):
    match = match.group()
    return re.sub("\<\/foreign\>", "", str(match))
df['utterance'] = [re.sub("\<\/foreign\>", my_replace_for_foreignend, str(x)) for x in df['utterance']]

def my_replace_for_foreignempty(match):
    match = match.group()
    return re.sub("\<foreign\slang=\"\w\w\w\"\s\/\>", "", str(match))
df['utterance'] = [re.sub("\<foreign\slang=\"\w\w\w\"\s\/\>", my_replace_for_foreignempty, str(x)) for x in df['utterance']]

# re.sub with custom function to clean the anonymized male name tags
def my_replace_for_anon(match):
    match = match.group()
    return re.sub("<anon ((type|nameType)=\"\w*\" ?)* \/>", "anoninfo", str(match))
df['utterance'] = [re.sub("<anon ((type|nameType)=\"\w*\" ?)* \/>", my_replace_for_anon, str(x)) for x in df['utterance']]


#print(df)
# check for pesky ">" or "<" in dataframe
found = df[df['utterance'].str.contains('>')]
print(found.count())

# write csv
df.to_csv(path_to_output + 'cleanframe.csv', index=False)