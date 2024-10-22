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
