# Project 1 - Calculate the Sample Size of a Dataset using Statistics

## Introduction

For this project, your goal is to design a program that uses statistics to help a developer select a test data (sample)
set from the complete data (population) set that is expected to be processed. Many times developers are asked to work
with large data sets that are impractical to use during development, since a large data set could take minutes to run
each time it is executed. Consider how many times you must run a program while developing it and imagine if it took five
minutes to run each time, it would be impractical to do this, so developers often need to create a much smaller dataset
to use during development. However, just selecting the first few records of a data set can lead to errors, since the
first few records may not represent an accurate sample of the data. Statistics offers a clever way of solving this
problem, since you can use a formula to calculate the correct sample size from a large data set to use for development.

In order to do this, you will need to design a program that takes the entire data set as the initial input, you will
then need to select the column / field, which represents the data point you're interested in using to create your sample
from. For example, if you're analyzing the number of team wins, you will need to pick the team wins' field to use as the
basis for selecting your sample data set. You would then use this to calculate the min, max, median, mode, mean,
standard deviation, and eventually the sample size of the population.

Once you have the total sample size, you will use this to create a sample data set by selecting representative records
of the min and max, and then fill in the remainder of the data set by randomly selecting the appropriate
number of records from your population (original large data set) and saving that new sample data set to disk, so that it
can be used for development. For example, let say you have a total population of 10,000 records, and you compute a
sample size of 300, you would then select records that represent the  (min, max) and then fill in the
remaining records with randomly selected records to create a total of 300 records from the original dataset and save
those records to disk. You cannot repeat records, each record must be unique. You are required to create a total of 15
test data files that are generated using the specified values for confidence interval and margin of error. By doing this
you will create a selection of files that can be used at various points in development, since as the program become more
complete you would increase the size of the input data to test various aspects of a program such as memory usage.

# Videos

1. [Lecture 1](https://youtu.be/JCQ_8ZlzhnY)
2. [Lecture 2](https://youtu.be/FfdZm-UoBdc)

# Your program is required to do the following:

1. Take this file as input: [state_population.csv](data/state_population.csv)
2. Use the population field as the datapoint to select your sample.
3. Set the margin of error (.01, .05, .10)
4. Calculate the following summary statistics for the selected field:
    1. Count, Min, Max, and Standard Deviation
    2. Sample Size at 80%, 85%, 90%, 95%, 99% confidence using .01, .05, .10 margin of error respectively

    * Note use .5 standard deviation instead of the actual standard deviation to calculate the sample size
5. Create test data file(s) that contain the number of values specified by the sample size; however, these files must
   contain records that include max and min of the selected data point from the
   original data set.
6. Output test data files to the output directory called "sample_files_output"
7. Your program should output 15 different files using the naming convention
    1. sample_data_confidenceInterval_marginError_recordCount.csv:
        * For example (counts are accurate):
            1. sample_data_number_1.28_0.1_22.csv
            2. sample_data_number_1.28_0.01_51.csv
            3. sample_data_number_1.28_0.05_39.csv
            4. sample_data_number_1.44_0.1_25.csv
            5. sample_data_number_1.44_0.01_51.csv
            6. sample_data_number_1.44_0.05_41.csv
            7. sample_data_number_1.65_0.1_29.csv
            8. sample_data_number_1.65_0.01_51.csv
            9. sample_data_number_1.65_0.05_43.csv
            10. sample_data_number_1.96_0.1_33.csv
            11. sample_data_number_1.96_0.01_51.csv
            12. sample_data_number_1.96_0.05_45.csv
            13. sample_data_number_2.58_0.1_39.csv
            14. sample_data_number_2.58_0.01_51.csv
            15. sample_data_number_2.58_0.05_48.csv

# Little Help

1. Look at my config class [here](app/config/__init__.py)
2. Look at my file utilities for making the path [here](app/file_ops/__init__.py)
3. DO NOT FORGET TO USE .5 for your population standard deviation or the program won't generate the correct output
   for my tests
4. Check my code [here](https://github.com/NJIT-WIS/sample_data_generator_project1-demo), it is not complete; however it might help and give you some ideas

## Z-Score Table

80% confidence => 1.28 z-score
85% confidence => 1.44 z-score
90% confidence => 1.65 z-score
95% confidence => 1.96 z-score
99% confidence => 2.58 z-score

You will be graded on:

1. All teacher tests passing: 45 Points
2. Code Grammar: 45 Points
3. Project 1 Canvas Quiz: 10 Points (See canvas Project 1 Module)

Grading Notes:

1. You will at least get 30 points for turning the project in even if it doesn't work at all. You will automatically get
   a total of 30 points for the assignment. Except not having code in the app folder, which results in a 0.
2. You will get a 0 if your application code is not in the app folder
3. You will lose points for repeating lines of code. 5-10 points
4. You will lose 10-20 points if the code does not follow separation of concerns
5. You will lose 10-20 points if it appears you did not try to follow SOLID
6. You will lose 10-20 points for not using classes
7. You will lose 10-20 points for not using the correct types of methods i.e. mainly you are using static methods

# Tips to complete this and Requirements

1. Read this article on min, max, range, median, and
   mode. [Click Here](https://www.ucd.ie/msc/t4media/Mean%20and%20Standard%20Deviation.pdf)
2. Read this article about how to calculate the standard
   deviation. [Click Here](https://www.wikihow.com/Calculate-Standard-Deviation)
3. Read this article about how to calculate a sample size.  [Click here](https://www.wikihow.com/Calculate-Sample-Size)
4. Read this article about how to read and write data with
   Pandas. [Click Here](https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/02_read_write.html#min-tut-02-read-write)
5. Read this tutorial about creating summary statistics with
   Pandas [Click Here](https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/06_calculate_statistics.html#min-tut-06-stats)
6. First do the sample calculation with the numbers from the WikiHow article, so you check your math
7. Refactor your working code to place it in the app folder. Note, you don't need to make an actual command line
   application, it just needs to work using tests, so you don't need a fully working program.
8. Your code needs to be module and follow separation of concerns, don't repeat yourself, and demonstrate SOLID to the
   best of your ability.
9. You can use Pandas for most of the functionality of the program, so once you know your steps, you should research
   how Pandas can be used do it.
10. Your final program should use static methods because you are mainly just sending commands to Pandas and Pandas
    dataframe is the data instance. Each Panda's command should be its own method, since you shouldn't directly call
    library functions.
11. You need to calculate directory paths programmatically, or your program won't work on GitHub because it won't be
    able to find the data directory path, since Github's test environment is not the same as your own computer.
    [Check here for my code](app/file_ops/__init__.py)
12. Your data selection algorithm must not select the same record twice, so that it results in the correct total number
    of records specified by the sample size.

## Steps to Complete the Assignment

1. Open Pycharm Pro / Pycharm Community and clone the assignment repository. Open up a terminal in Pycharm, run "pip3
   install -r requirements.txt" and then run "pytest".  **If pycharm shows you an error about pip / requirements when
   you clone the repo just skip/cancel/dismiss the error and run the command in the terminal like I said above**
2. When your pytest --pylint passes just commit and push it back to the origin and the assignment will be graded
   automatically by GitHub running the test that you run locally.
3. Check that your tests pass on GitHub after you push the assignment and then submit a link to your repository to the
   assignment in Canvas. In GitHub on the repository, click the actions tab on GitHub to see your tests run. You will
   need to click on the autograding workflow to inspect that screen to see the detail test results.


