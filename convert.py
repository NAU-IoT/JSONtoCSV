import sys
import os
import csv
import json

# Reads CSV and writes to JSON
def csv_to_json(input_file, output_file):
    with open(input_file, 'r') as csvfile, open(output_file, 'w') as jsonfile:
        fieldnames = csvfile.readline().strip().split(',')
        reader = csv.DictReader(csvfile, fieldnames)
        json.dump(list(reader), jsonfile, indent=2)

# Reads JSON and writes to CSV
def json_to_csv(input_file, output_file):
    with open(input_file, 'r') as jsonfile, open(output_file, 'w') as csvfile:
        data = json.load(jsonfile)
        fieldnames = list(data[0].keys())
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            writer.writerow(row)

def main():
    # If there aren't 3 arguments, print the intended usage and exit
    if len(sys.argv) != 3:
        print("Usage: convert.py input_file output_file")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Collect file extensions for csv/json check
    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()

    # CSV -> JSON
    if input_ext == '.csv' and output_ext == '.json':
        csv_to_json(input_file, output_file)
    # JSON -> CSV
    elif input_ext == '.json' and output_ext == '.csv':
        json_to_csv(input_file, output_file)
    else:
        print("Unsupported conversion. Please provide input and output files with .csv or .json extensions.")
        sys.exit(1)

if __name__ == "__main__":
    main()
