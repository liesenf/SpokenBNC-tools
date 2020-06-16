# Tools for preprocessing SpokenBNC dataset

Here are Python scripts for processing SpokenBNC data. The SpokenBNC 2014 is a collection of 1251 transcribed conversations.
More information: http://corpora.lancs.ac.uk/bnc2014/

## 1: XML to csv

SpokenBNC data comes in XML format. The following scripts extract information as dataframes (.csv), with the option to preserve xml tag content or discard it. Use the following scripts to extract content from SpokenBNC's XML files in batches and write it to .csv dataframes. The batch_xml_to_csv script read .xml files, extract Utterance ID [UID], Speaker ID [Speaker] and utterance content [Utterance] from "body/\<u> ... \</u>", and create a dataframe with colums [UID, Speaker, Utterance] and utterance content as rows.

### batch_xml_to_csv_simplified
The simplified version extracts utterance text of <u> and discards utterance tags and tag content.

### batch_xml_to_csv_complete
The complete version extracts utterance text of <u> including text and all tags (and their xml format).
  
## 2: concatenating and cleaning csv
  
  ### concat_dataframe.py
  ### clean.py
  
## 3. create subcorpora
  
  ### speaker_metadata.py
  ### split_subcorpora.py


