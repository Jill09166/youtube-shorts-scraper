thonimport json
import csv

def export_data(data, filename):
    """
    Export scraped data to a specified file format (JSON by default).

    Args:
    - data (list): The scraped data to be exported.
    - filename (str): The name of the file to save the data to.
    """
    if filename.endswith('.json'):
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    elif filename.endswith('.csv'):
        with open(filename, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)