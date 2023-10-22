"""
Program Name: Weather Data Aggregator
Author: Jason Armstrong
Date: 2023-10-21
Version: 1.0

Description:
    This program is a command-line tool that aggregates weather data from Chicago beaches.
    It reads a CSV file containing weather data and outputs another CSV file with daily aggregates
    for each weather station. The aggregates include the start, end, high, and low air temperatures
    for each day.

Usage:
    The program reads data from STDIN and writes the output to STDOUT. It can be used as follows:
    `cat data/chicago_beach_weather.csv | python3 interview/__main__.py > output.csv` from the
    root of repository.

Requirements:
    - Python 3.x
    - csv module (Standard Library)
    - datetime module (Standard Library)

Input CSV Format:
    Station Name, Measurement Timestamp, Air Temperature, ...

Output CSV Format:
    Station Name, Date, Min Temp, Max Temp, First Temp, Last Temp

Performance:
    The program is designed to process the data without loading it all into memory at once.

Tests:
    python-interview/test/weather_test.py. Run with `make test` from root of repository

Notes:
    - The program assumes that the input data will be consistent with the example provided.
    - The output must be valid CSV, with the correct number of columns and a header.

License:
    ...
"""
import csv
from datetime import datetime
from typing import TextIO


def process_csv(reader: TextIO, writer: TextIO) -> None:
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
            data = aggregated_data[station_name][date]  # Note: `data` is a reference to and not a copy of the row on the RHS.
                                                        #        Updates to data updates the entry in `aggregated_data` for
                                                        #        that station.
            data['Min Temp'] = min(data['Min Temp'], temperature)
            data['Max Temp'] = max(data['Max Temp'], temperature)

            if timestamp < data['First Time']:
                data['First Time'] = timestamp
                data['First Temp'] = temperature

            if timestamp > data['Last Time']:
                data['Last Time'] = timestamp
                data['Last Temp'] = temperature

    #4. Writing the aggregated data to 'writer'
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
# End process_csv()
