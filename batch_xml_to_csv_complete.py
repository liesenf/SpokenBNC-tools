# -*- coding: utf-8 -*-
"""
This script batch extracts content from xml files and writes it to csv files.
Built for SpokenBNC corpus data (http://corpora.lancs.ac.uk/bnc2014/).
Simplified version extracts only text from utterances ("body/u").
Complete version extracts all content of utterances ("body/u"), including content from nested texts such as "vocal", "pause", "anon", "event", "unclear".
See corpus annotation manual for complete tag list.

Created June 2020 at HK PolyU
@author Andreas Liesenfeld
"""

import xml.etree.ElementTree as et
import pandas as pd
import os

# input and output paths
path = '/home/andreas/Desktop/SpokenBNC/spoken/test'
path_to_output = r'/home/andreas/Desktop/SpokenBNC/spoken/csvtest/'

    # read files in path directory
for filename in os.listdir(path):
    if not filename.endswith('.xml'): continue # read only xml files
    fullname = os.path.join(path, filename)
    parsed_xml = et.parse(fullname)

    # create empty dataframe with three columns for extracted content
    dfcols = ['UID', 'speaker', 'utterance']
    df_xml = pd.DataFrame(columns=dfcols)

    # extract specified content from xml file:
    # utterance ID as UID, speaker ID as speaker, utterance content as utterance
    for turn in parsed_xml.findall('body/u'):
        uid = turn.attrib.get('n')
        speaker = turn.attrib.get('who')
        utterance = et.tostring(turn, encoding='us-ascii', method='xml').decode('utf8')

        # append extracted content to dataframe
        df_xml = df_xml.append(
            pd.Series([uid, speaker, utterance], index=dfcols),
            ignore_index=True)
        # write each dataframe to path_to_output as separate csv file
        df_xml.to_csv(path_to_output + filename+'.csv', index=False)

    print("Conversion complete: " + filename)
print("Done")
