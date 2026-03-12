#!/usr/bin/env python3
"""
Author: Keaton Gobrecht
Email: kgobrecht@madisoncollege.edu
Description: <Semester long script which analyzes an Apache web log to determine if the highest-hitting IP address is a current threat.>
"""
import sys 

listOfYs = ['y', 'yes', 'yep', 'yup', 'yeah']

if len(sys.argv) > 1:
    strContinue = sys.argv[1].lower()
else:    
    strContinue = input("Would you like to continue?    (y/n)\n>>>> ").lower()

if strContinue in listOfYs:

    with open("06_CP-Access.log", "r") as wrapperLogFile:
        strLogLines = wrapperLogFile.read()

    listLogLines = strLogLines.split("\n")
    
    with open("milestone06analysis.txt", "w") as wrapperLogFile:
     
        for strLogLine in listLogLines:
            listLogLine = strLogLine.split(" ")
            strIPAddress = listLogLine[0]
            strIPReturnCode = listLogLine[8]
            strIPReturnCode = f"{strIPAddress} - {strIPReturnCode}"
            if strIPReturnCode >= '400':
                print(strIPReturnCode)
                if strIPReturnCode >= '500':
                    wrapperLogFile.write(f"{strIPReturnCode}\n")

