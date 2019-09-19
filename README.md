# Aquatic's General Purpose Programming Interview

If you have an on-site interview at Aquatic, you'll use this prepared workspace to solve the programming problem described below. We're sharing it with everyone to ensure a level playing field when it comes to knowledge about technical interviews in the finance industry.

During your interview, you'll work along side another Aquatic software engineer to write the code and come up with a complete working solution in about 2 hours. You'll be able to look things up on the Internet, just as you would on any regular working day. Along the way, the requirements may change, so be prepared to make adjustments accordingly.

If you prefer, you can solve this problem on your own time, using your own computer. Fork the project, and be sure to have your finished solution pushed to Github when you arrive for your interview. When you get here, you'll spend some additional time changing it while working along side another Aquatic software engineer.

## The Problem

Included in this repository is a data set taken from the [City of Chicago's Open Data portal](https://data.cityofchicago.org/). It has weather data from Chicago beaches in CSV format.

You'll need to write a command line tool in Python that turns the (roughly) one hour temperature samples into daily aggregates, with the start, end, high, and low of all the values of the Air Temperature for each day, at each weather station. For example, assuming the temperature values on a particular day at a particular station were:

```
01/01/2016 11:00:00 PM,69
01/01/2016 08:00:00 PM,70
01/01/2016 07:00:00 PM,70
01/01/2016 06:00:00 PM,72
01/01/2016 05:00:00 PM,72
01/01/2016 04:00:00 PM,73
01/01/2016 03:00:00 PM,69
01/01/2016 02:00:00 PM,70
01/01/2016 01:00:00 PM,70
01/01/2016 12:00:00 PM,70
01/01/2016 11:00:00 AM,70
01/01/2016 10:00:00 AM,70
01/01/2016 09:00:00 AM,70
01/01/2016 08:00:00 AM,71
01/01/2016 07:00:00 AM,72
01/01/2016 06:00:00 AM,72
01/01/2016 05:00:00 AM,71
01/01/2016 04:00:00 AM,69
01/01/2016 03:00:00 AM,67
01/01/2016 02:00:00 AM,64
01/01/2016 01:00:00 AM,67
01/01/2016 12:00:00 AM,67
```

Then the expected values for start, end, high, and low for this day would be:

* start: 67
* end: 69
* high: 73
* low: 64

The program should read the data from STDIN and output the aggregated data to STDOUT in CSV format. The exact details of the output format are up to you.

## Problem Environment

This repository has a Makefile, prepared for a Linux environment, with various targets for running tests and executing the program. If you're not familiar with [make](http://matt.might.net/articles/intro-to-make/), don't worry. You'll just need to use a few commands, all of which will be shown if you run the `make` command in the root directory of the repository.

```
aquanauts/interview$ make
repl                           Run an iPython REPL
run                            Run the program on the provided dataset
test                           Run tests
watch                          Run unit tests continuously
```

For example, to run the tests, you run `make test`. The `watch` target will run the tests automatically whenever you change a `.py` file. Any of these targets will automatically install all the necessary dependencies (including miniconda3) to the repository directory.

You are encouraged take a few minutes to clone this repository and experiment with this environment before your interview, so that it is familiar to you when you arrive. Feel free to ask any questions if you run into problems.
