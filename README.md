# Edgar-Analytics (Insight Data Engineering Coding Challenge)
This repository includes my solution to the insight Data Engineering coding challenge for edgar-analytics. 
# Directory Structure
The directory structure for this repo looks like this:

    ├── README.md 
    ├── run.sh
    ├── src
    │   └── sessionization.py
    ├── input
    │   └── inactivity_period.txt
    │   └── log.csv
    ├── output
    |   └── sessionization.txt
    ├── insight_testsuite
        └── run_tests.sh
        └── tests
            └── test_1
            |   ├── input
            |   │   └── inactivity_period.txt
            |   │   └── log.csv
            |   |__ output
            |   │   └── sessionization.txt
            ├── test_2
            |   ├── input
            |   │   └── inactivity_period.txt
            |   │   └── log.csv
            |   |── output
            |        └── sessionization.txt
            ├── test_3
                ├── input
                │   └── inactivity_period.txt
                │   └── log.csv
                |── output
                    └── sessionization.txt
# Resources and Dependencies
 * Python 3.6 or higher
 * libraries 
     * sys
     * datetime
     * csv
    
# Running Code
To run code for this repo, you need to compile run.sh with the input folder containing two files inactivity_period.txt and log.csv. Output file generated would be sessionization.txt.    
Example to run this code: 
```edgar-analytics~$ sh run.sh```
    
# Implementation details

This program expects two input files :

* `log.csv`: EDGAR weblog data
* `inactivity_period.txt`: Holds a single value denoting the period of inactivity that should be used to identify when a user session is over

Sessionization.py in the src directory, is the code to run this solution. Output of this code will be generated as sessionization.txt in the output directory.


