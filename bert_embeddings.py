import pandas as pd
import torch
from transformers import BertTokenizer, BertModel
import re
import csv

# Load city names from a CSV file
def load_city_names_from_csv(csv_file_path):
    df = pd.read_csv(csv_file_path)
    # Assuming the first column contains the city names
    cities = df.iloc[:, 0].dropna().tolist()  # Drop any NaN values
    return [city.strip() for city in cities]  # Remove any leading/trailing whitespace

# Load content from the old book
def load_book_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

# Load the BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Function to get BERT embeddings for city names
def get_city_embeddings(cities, book_content):
    embeddings = {}
    for city in cities:
        # Find sentences containing the city name
        pattern = r'([^.]*?\b' + re.escape(city) + r'\b[^.]*\.)'  # Regex to find sentences
        sentences = re.findall(pattern, book_content, re.IGNORECASE)
        
        city_embeddings = []
        for sentence in sentences:
            # Get context (50 characters before and after the city name)
            start_index = max(sentence.lower().index(city.lower()) - 50, 0)
            end_index = min(start_index + len(city) + 100, len(sentence))
            context = sentence[start_index:end_index]

            # Tokenize and get embeddings
            inputs = tokenizer(context, return_tensors='pt', padding=True, truncation=True)
            with torch.no_grad():
                outputs = model(**inputs)
                embedding = outputs.pooler_output.squeeze().numpy()  # Get pooled output
            city_embeddings.append((context, embedding))

        embeddings[city] = city_embeddings
    return embeddings

# Save embeddings to a CSV file
def save_embeddings_to_csv(embeddings_dict, output_csv_path):
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['City', 'Context', 'Embedding'])  # Write header
        for city, contexts in embeddings_dict.items():
            for context, embedding in contexts:
                embedding_str = ', '.join(map(str, embedding))
                writer.writerow([city, context, embedding_str])  # Write each row
    print(f'Saved embeddings to {output_csv_path}')

# Main function to execute the workflow
def main():
    city_file_path = r'C:\Users\User\Documents\random py scripts\thesis\nomic.ai\livytagged.csv'  # Path to your CSV file with city names
    book_file_path = r'C:\Users\User\Documents\random py scripts\thesis\nomic.ai\livy.txt'  # Path to your book text file
    output_csv_path = r'C:\Users\User\Documents\random py scripts\thesis\nomic.ai\city_embeddings.csv'  # Output CSV path
    
    cities = load_city_names_from_csv(city_file_path)
    book_content = load_book_content(book_file_path)
    
    # Get BERT embeddings for each city
    embeddings_dict = get_city_embeddings(cities, book_content)

    # Save results to a CSV file
    save_embeddings_to_csv(embeddings_dict, output_csv_path)

if __name__ == "__main__":
    main()
