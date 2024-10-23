# WordEmbeddings
The python scripts I used to prepare files to be processed in Nomic AI and bert Word Vectors like BERT


There are 7 txt files:
Herodotus, Histories
Cicero, On The Republic
Livy, Ab Urbe Condita Libri, History of Rome
Pliny the Elder, Natural History
Strabo, Geographica 
Plutarch’s Parallel Lives
Dionysius of Halicarnassus, Roman Antiquities

Embarassingly these are English translations, I meant to have versions of the original languages, but I wanted to optimize my process first.

Allplaces.csv, and allplacesshorter.csv, is a compiled list of ancient roman sites from the Romurbital and Pleiades archive.  The Pleiades archive is too big, so I removed it, leaving onlya few words in that column, but still keeping all sites listed in the Romurbital.

These files are meant to be used by the 'listwordsfortagging.py"

#listwordsfortagging.py

This script has a database of terms that I want to know if they are in the ancient historian's book or not. It looks for geographic features terminologies and for the words listed in the allplacesshorter.csv.  I hope to expand on this list in the future.

Its output is a csv file with column 1 being all the relative words found in the txt, and column 2 gives its category (Geo_feature, unidentified, Romurbital, Plieades, etc)
To use it, you need to only update file paths to the txt you want to examine, and the pathfile to allplacesshorter.csv

#taggcsv.py

This python script uses the output of the listwordsfortagging.py, to make a listing of all instances of your list of words, and gives the context in the second column, currently it take 50 characters before and after the word.  This needs to change to make sure it doesn't cut words or sentences, so I will edit this script in due time.

This output can be uploaded to nomic.ai

It also can be used with wordvectors python scripts, such as roberta2_output.py and bert_embeddings.py
These two script will create a TSNE visualization and and output csv which holds all the embeddings.

BERT model (Bidirectional Encoder Representations from Transformers) is a word vector model which focuses on capturing the context for the word.
Roberta model is simular to BERT but it does not have next sentence prediction (and other things that I will explain in the near future.
