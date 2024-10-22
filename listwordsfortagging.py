import pandas as pd
import re

# List of geographic features
geo_features = {
    'river', 'rivers', 'mountain', 'mountains', 'hill', 'hills', 'sea', 'seas', 'lake', 'lakes',
    'forest', 'forests', 'valley', 'valleys', 'water', 'waters', 'shore', 'shores', 'coast', 'coasts',
    'ocean', 'oceans', 'mount', 'mounts', 'beach', 'beaches', 'camp', 'camps', 'plain', 'plains',
    'plateau', 'plateaus', 'cave', 'caves', 'spring', 'springs', 'swamp', 'swamps', 'desert', 'deserts',
}

# List of official words
official_words = {
    'abala', 'abella', 'abellinum', 'abellinum marsicum', 'abolani', 'accienses', 'acerrae', 'acerrae vafriae', 'aceruntia'
}

# Load the Pleiades names, Romurbital places, and Unidentified places from the CSV
pleiades_file_path = r'C:\Users\User\Documents\random py scripts\thesis\nomic.ai\allplacesshorter.csv'
pleiades_df = pd.read_csv(pleiades_file_path, encoding='ISO-8859-1')

# Ensure necessary columns are present
required_columns = {'title', 'romurbital', 'unidentified'}
if not required_columns.issubset(pleiades_df.columns):
    raise KeyError("The Pleiades CSV file must contain 'title', 'romurbital', and 'unidentified' columns")

# Convert relevant columns to sets of lowercased words for fast lookup
pleiades_words = set(pleiades_df['title'].dropna().str.lower())
romurbital_places = set(pleiades_df['romurbital'].dropna().str.lower())
unidentified_places = set(pleiades_df['unidentified'].dropna().str.lower())

# Combine only the required sets to check against the TXT file
all_words_to_check = geo_features | official_words | pleiades_words | romurbital_places | unidentified_places

# Path to your TXT file
txt_file_path = r'C:\Users\User\Documents\random py scripts\thesis\nomic.ai\livy.txt'

# Read the TXT file, convert to lowercase, and use regular expressions to tokenize words
with open(txt_file_path, 'r', encoding='ISO-8859-1') as file:
    content = file.read().lower()  # Convert to lowercase

# Tokenize by splitting on non-alphanumeric characters to handle punctuation
words_from_txt = set(re.findall(r'\b\w+\b', content))

# Print debug information for the first 100 words to verify
print(f"Sample words from the TXT file: {list(words_from_txt)[:100]}")

# Find matches between the words in the TXT file and all words to check
words_found = all_words_to_check.intersection(words_from_txt)

# Create a list to hold the results with categories
results = []

# Categorize each found word
for word in words_found:
    if word in geo_features:
        category = 'Geographic Feature'
    elif word in official_words:
        category = 'Official Word'
    elif word in pleiades_words:
        category = 'Pleiades Title'
    elif word in romurbital_places:
        category = 'Romurbital Place'
    elif word in unidentified_places:
        category = 'Unidentified Place'
    else:
        category = 'Unknown'

    results.append({'Word': word, 'Category': category})

# Create a DataFrame from the results
found_df = pd.DataFrame(results)

# Save the found words to a CSV file
output_file_path = r'C:\Users\User\Documents\random py scripts\thesis\nomic.ai\words_found_in_livy.csv'
found_df.to_csv(output_file_path, index=False)

print(f'Words found in TXT file have been saved to {output_file_path}')
