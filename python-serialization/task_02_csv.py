import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Convert CSV data to JSON format and write to data.json.

    Parameters:
    csv_filename (str): The filename of the input CSV file.

    Returns:
    bool: True if conversion was successful, False otherwise.
    """
    try:
        # Read CSV data
        with open(csv_filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]
        
        # Write JSON data
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        
        return True
    except FileNotFoundError:
        print(f"Error: The file {csv_filename} was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
