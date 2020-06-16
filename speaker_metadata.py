# -*- coding: utf-8 -*-
"""
This script reads the "bnc2014spoken-speakerdata.tsv" file and extracts speakerIDs from it
based on various metadata criteria such as age and gender categories.
Then it saves the extracted SpeakerIDs in a pickle outfile and prints the n of SpeakerIDs for each category.
Edit "pickle.dump(ID_list_old_f, fp)" to select which list is saved as pickle outfile.
See corpus annotation manual for complete tag list.

Created June 2020 at HK PolyU
@authors Andreas Liesenfeld and Gabor Parti
"""


import pandas as pd
import pickle

#input output paths
path = r'/home/andreas/Desktop/SpokenBNC/spoken/metadata/'
path_to_output = r'/home/andreas/PycharmProjects/spokenbncdataset/cleaning/cleaned/'

#read dataframe and add column names
df = pd.read_csv(path + 'bnc2014spoken-speakerdata.tsv', index_col=None, header=None, sep='\t', names=['SpeakerID', 'exactage', 'age1994', 'agerange', 'gender', 'nat',  'birthplace', 'birthcountry', 'l1', 'lingorig', 'dialect_rep',
                                            'hab_city', 'hab_country', 'hab_dur', 'dialect_l1', 'dialect_l2', 'dialect_l3', 'dialect_l4', 'edqual', 'occupation', 'socgrade', 'nssec',
                                           'l2','fls','in_core'])

# selecting rows by column name based on condition and save as list
# gender m and f
ID_list_gender_m = df[df['gender'] == 'M']['SpeakerID'].to_list()
ID_list_gender_f = df[df['gender'] == 'F']['SpeakerID'].to_list()

## age above and below 30
agerange_young = ['0_10', '11_18', '19_29']
agerange_old = ['30_39', '40_49', '50_59', '60_69', '70_79', '80_89', '90_99']

ID_list_agerange_young = df.query('(agerange in @agerange_young)')['SpeakerID'].to_list()
ID_list_agerange_old = df.query('(agerange in @agerange_old)')['SpeakerID'].to_list()

## age and gender combined (can be edited to include other values eg SES)
gender_female = ['F']
gender_male = ['M']
ID_list_old_f = df.query('(agerange in @agerange_old) & (gender in @gender_female)')['SpeakerID'].to_list()
ID_list_old_m = df.query('(agerange in @agerange_old) & (gender in @gender_male)')['SpeakerID'].to_list()
ID_list_young_f = df.query('(agerange in @agerange_young) & (gender in @gender_female)')['SpeakerID'].to_list()
ID_list_young_m = df.query('(agerange in @agerange_young) & (gender in @gender_male)')['SpeakerID'].to_list()

# ## print n and speaker ID of lists
#print('List of Speaker IDs: ', ID_list_gender_f)
print('n of female is:', len(ID_list_gender_f))
print('n of male is:', len(ID_list_gender_m))
print('n of old is:', len(ID_list_agerange_old))
print('n of young is:', len(ID_list_agerange_young))
print('n of young+female is:', len(ID_list_young_f))
print('n of young+male is:', len(ID_list_young_m))
print('n of old+female is:', len(ID_list_old_f))
print('n of old+male is:', len(ID_list_old_m))


## SELECT OUTFILE HERE: save any lst with pickle
with open('outfile', 'wb') as fp:
    pickle.dump(ID_list_old_m, fp)
print('Selected IDs successfully saved as pickle outfile')



