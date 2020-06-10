# Tools for preprocessing the SpokenBNC dataset

Here are scripts for processing SpokenBNC data. The SpokenBNC 2014 is a collection of 1251 transcribed conversations.
More information: http://corpora.lancs.ac.uk/bnc2014/

## 1: XML to dataframe

SpokenBNC data comes in XML format. The following scripts extract information as dataframes (.csv), with the option to preserve xml tag content or discard it. Use the following scripts to extract content from SpokenBNC's XML files in batches and write it to .csv dataframes.

### batch_xml_to_csv_simplified

This script extracts Utterance ID, Speaker ID and utterance content. The simplified version discards utterance tags, only utterance text is extracted.

### batch_xml_to_csv_complete

This script extracts Utterance ID, Speaker ID and utterance content. This complete version preserves utterance tags.


