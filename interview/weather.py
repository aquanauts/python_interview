import csv

def process_csv(reader, writer):
    csv_reader = csv.reader(reader)
    for row in csv_reader:
        # Your aggregation logic will go here
        pass
    # Once aggregation is done, you'll write the output to 'writer'
