# Aquatic's Python Programming Interview

If you have an on-site python interview at Aquatic, you'll use this prepared workspace to solve the programming problem described below. We're sharing it with everyone to ensure a level playing field when it comes to knowledge about technical interviews in the finance industry.

During your interview, you'll work along side another Aquatic software engineer to write the code and come up with a complete working solution in 2 hours. You'll be able to look things up on the Internet, just as you would on any regular working day. You'll use a Linux workstation (like the ones we use) to write the code with an editor of your choice. Along the way, the requirements may change, so be prepared to make adjustments accordingly. We'll try to make this experience as realistic as possible, so you can get a sense of what working at Aquatic is really like.

Here are some of the criteria by which you'll be evaluated:

  * Can you create an effective solution in the time given? Does it actually run?
  * Can you adapt your solution to new requirements?
  * Can you explain what you're doing and why?
  * Can you maintain good project hygiene, treating this like "real world" software.

If you prefer, you can solve this problem on your own time, using your own computer (Linux recommended). Then, once you arrive at Aquatic for your interview, you'll spend some time working with another engineer to adapt your solution to new requirements. See the section below for instructions. 

## The Problem

Included in this repository is a data set taken from the [City of Chicago's Open Data portal](https://data.cityofchicago.org/). It has weather data from Chicago beaches in CSV format.

You'll need to write a command line tool in Python that turns the (roughly) one hour temperature samples into daily aggregates, with the start, end, high, and low of all the values of the Air Temperature for each day, at each weather station. For example, assuming the temperature values on a particular day at a particular station were:

```
Foster Weather Station,01/01/2016 11:00:00 PM,69
Foster Weather Station,01/01/2016 08:00:00 PM,70
Foster Weather Station,01/01/2016 07:00:00 PM,70
Foster Weather Station,01/01/2016 06:00:00 PM,72
Foster Weather Station,01/01/2016 05:00:00 PM,72
Foster Weather Station,01/01/2016 04:00:00 PM,73
Foster Weather Station,01/01/2016 03:00:00 PM,69
Foster Weather Station,01/01/2016 02:00:00 PM,70
Foster Weather Station,01/01/2016 01:00:00 PM,70
Foster Weather Station,01/01/2016 12:00:00 PM,70
Foster Weather Station,01/01/2016 11:00:00 AM,70
Foster Weather Station,01/01/2016 10:00:00 AM,70
Foster Weather Station,01/01/2016 09:00:00 AM,70
Foster Weather Station,01/01/2016 08:00:00 AM,71
Foster Weather Station,01/01/2016 07:00:00 AM,72
Foster Weather Station,01/01/2016 06:00:00 AM,72
Foster Weather Station,01/01/2016 05:00:00 AM,71
Foster Weather Station,01/01/2016 04:00:00 AM,69
Foster Weather Station,01/01/2016 03:00:00 AM,67
Foster Weather Station,01/01/2016 02:00:00 AM,64
Foster Weather Station,01/01/2016 01:00:00 AM,67
Foster Weather Station,01/01/2016 12:00:00 AM,67
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
patch                          Generate a patch file to submit for your solution
repl                           Run an iPython REPL
run                            Run the program on the provided dataset
test                           Run tests
watch                          Run unit tests continuously
```

For example, to run the tests, you run `make test`. The `watch` target will run the tests automatically whenever you change a `.py` file. Any of these targets will automatically install all the necessary dependencies (including miniconda3) to the repository directory.

You are encouraged take a few minutes to clone this repository and experiment with this environment before your interview, so that it is familiar to you when you arrive. Feel free to ask any questions if you run into problems.

## Submitting an At-Home Solution

If you've chosen to complete the first iteration of this exercise at home, here's how you can submit your solution to Aquatic:

#### Run `make patch`

When you've completed the exercise and are happy with the result, run `make patch` from the command line, in the root of the repository. This will generate a file named `aquatic_interview_solution.patch`.

#### Submit Your Solution

Once you've generated a patch file, you can send it to us using the link provided by your contact at Aquatic. If you run into problems, or have questions, feel free to reach out and ask!

