import csv
import re

# Function to load location names from the CSV and convert them to lowercase
def load_locations(csv_file):
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        locations = [row[0].strip().lower() for row in reader]  # Assumes locations are in the first column and lowers them
    return locations

# Function to tag locations and extract context
def extract_location_context(text, locations):
    tagged_data = []
    for location in locations:
        # Use regex to find whole words and avoid partial matches, case-insensitive
        matches = re.finditer(rf'\b{re.escape(location)}\b', text, re.IGNORECASE)
        for match in matches:
            # Capture surrounding context (e.g., 50 characters before and after the location)
            start = max(match.start() - 200, 0)
            end = min(match.end() + 200, len(text))
            context = text[start:end]
            tagged_data.append([location, context])
    return tagged_data

# Main function to save data as CSV
def save_tagged_data_to_csv(input_text_file, csv_file, output_csv):
    # Load locations from the CSV file
    locations = load_locations(csv_file)
    
    # Read and lowercase the text from the file
    with open(input_text_file, mode='r', encoding='utf-8') as file:
        text = file.read().lower()  # Convert text to lowercase

    # Extract location and context
    tagged_data = extract_location_context(text, locations)

    # Save the extracted data into a CSV file
    with open(output_csv, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Location", "Context"])  # Write headers
        writer.writerows(tagged_data)

    print(f"Tagged data saved to {output_csv}")

# Example usage:
input_text_file = r'C:\Users\User\Documents\random py scripts\thesis\nomic.ai\cicerotherepublic.txt'
csv_file = r'C:\Users\User\Documents\random py scripts\thesis\nomic.ai\words_found_in_cicerotherepublic.csv'
output_csv = r'C:\Users\User\Documents\random py scripts\thesis\nomic.ai\cicerotherepublic_tagged.csv'

# Run the function to save to CSV
save_tagged_data_to_csv(input_text_file, csv_file, output_csv)
