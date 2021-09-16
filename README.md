# Aquatic's Python Programming Interview

If you have a software engineering interview at Aquatic, we'll ask you to use this prepared workspace to solve the problem described below. We're sharing it with everyone to ensure a level playing field when it comes to knowledge about technical interviews in the finance industry.

This exercise has two parts. First, we'll ask you to solve it at home on either a Mac or Linux computer. If you don't have access to a computer like that, contact us, and we'll arrange to provide you with a development environment. We expect that solving this will take you an hour or two. When you're finished, generate a patch file and send it to us (instructions below). Here are some of the things we'll be looking for in your solution:

  * Can you clone and set up this workspace in either Linux or OS X?
  * Can you create an effective solution in a reasonable amount of time? Does it actually work?
  * Did you add any unnecessary complexity?
  * Do you understand the data?
  * Is it well tested?
  * Can you maintain good project hygiene, treating this like "real world" software that you would want to maintain in perpetuity?

For the second part, we'll pair you up with another Aquatic engineer to review your solution and add some new functionality to it. 

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

### Output format

The program should read the data from STDIN and output the aggregated data to STDOUT in CSV format. The resulting CSV should follow this format:

```
Station Name,Date,Min Temp,Max Temp,First Temp,Last Temp
Foster Weather Station,01/01/2016,64.0,73.0,67.0,69.0
Foster Weather Station,01/02/2016,21.0,32.0,22.1,30.3
...
```

### Some things to consider
* For this first part of the exercise, you can assume the input data will be consistent with [the example](https://github.com/aquanauts/python_interview/blob/master/data/chicago_beach_weather.csv)
* The output must include a header, as specified above
* The output must use the same date format as the input (i.e. MM/DD/YYYY)
* The output must preserve the precision of floating point numbers while appending trailing zeros to whole numbers. This is often the default behavior in Python. Examples include:
    * `30.3` -> `30.3`
    * `73` -> `73.0`
    * `12.34` -> `12.34`
* The sort order of the output data rows is not important
* If you add Python packages to the project, be sure to add them to the [environment file](https://github.com/aquanauts/python_interview/blob/master/environment.yml), otherwise we won't be able to run your code.
* Ensure that the tests are passing (via `make test`) and the program runs (via `make run`) when you submit your solution

## Problem Environment

This repository has a Makefile, prepared for Linux or OS X, with various targets for running tests and executing the program. If you're not familiar with [make](http://matt.might.net/articles/intro-to-make/), don't worry. You'll just need to use a few commands, all of which will be shown if you run the `make` command in the root directory of the repository.

```
aquanauts/interview$ make
jupyter                        Run a jupyter notebook
patch                          Generate a patch file to submit for your solution
repl                           Run an iPython REPL
run                            Run the program on the provided dataset
test                           Run tests
watch                          Run unit tests continuously
```

For example, to run the tests, you run `make test`. The `watch` target will run the tests automatically whenever you change a `.py` file. Any of these targets will automatically install all the necessary dependencies (including miniconda3) to the repository directory.

You are encouraged take a few minutes to clone this repository and experiment with this environment before your interview, so that it is familiar to you when you arrive. Feel free to ask any questions if you run into problems.

## Submitting Your Solution

Here's how you can submit your solution to Aquatic.

#### Run `make patch`

When you've completed the exercise and are happy with the result, run `make patch` from the command line, in the root of the repository. This will generate a file named `aquatic_interview_solution.patch`.

#### Submit Your Solution

Once you've generated a patch file, you can send it to us using the link provided by your contact at Aquatic. If you run into problems, or have questions, feel free to reach out and ask!

