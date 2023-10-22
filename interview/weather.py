import csv
from datetime import datetime

def process_csv(reader, writer):
    aggregated_data = {}  # Initialize the nested dictionary
    csv_reader = csv.reader(reader)
    header = next(csv_reader)  # Skip the header row

    for row in csv_reader:
        # Extract relevant data from the current row
        station_name = row[0]
        timestamp_str = row[1]
        timestamp = datetime.strptime(timestamp_str, '%m/%d/%Y %I:%M:%S %p')  # Convert to date object to ascertain first and last day temp thru relational operations
        date = timestamp.date()
        temperature = float(row[2])

        # Step 1: Check if station_name exists
        if station_name not in aggregated_data:
            aggregated_data[station_name] = {}

        # Step 2: Check if date exists under station_name
        if date not in aggregated_data[station_name]:
            aggregated_data[station_name][date] = {
                'Min Temp': temperature,
                'Max Temp': temperature,
                'First Temp': temperature,
                'Last Temp': temperature,
                'First Time': timestamp,
                'Last Time': timestamp
            }

        # Step 3: Update existing target values
        else:
            data = aggregated_data[station_name][date]
            data['Min Temp'] = min(data['Min Temp'], temperature)
            data['Max Temp'] = max(data['Max Temp'], temperature)

            if timestamp < data['First Time']:
                data['First Time'] = timestamp
                data['First Temp'] = temperature

            if timestamp > data['Last Time']:
                data['Last Time'] = timestamp
                data['Last Temp'] = temperature

    # Writing the aggregated data to 'writer'
    csv_writer = csv.writer(writer)
    csv_writer.writerow(['Station Name', 'Date', 'Min Temp', 'Max Temp', 'First Temp', 'Last Temp'])  # Write header

    for station_name, dates in aggregated_data.items():
        for date, data in dates.items():
            row = [
                station_name,
                date.strftime('%m/%d/%Y'),  # Convert date object to string
                data['Min Temp'],
                data['Max Temp'],
                data['First Temp'],
                data['Last Temp']
            ]
            csv_writer.writerow(row)
