#!/usr/bin/env python3
"""
Author: Keaton Gobrecht
Description: Milestone 6
"""
import sys

listOfAcceptableValues = ['y', 'yes', 'yep', 'yup', 'yeah']

if len(sys.argv) > 1:
    strContinue = sys.argv[1].lower()
else:
    strContinue = input("Would you like to continue?  (y/n)\n>>>> ").lower()

if strContinue in listOfAcceptableValues:

    with open("06_CP-Access.log", "r") as wrapperLogFile:
        strLogLines = wrapperLogFile.read()

    listLogLines = strLogLines.split('\n')

    with open("milestone06analysis.txt", "w") as wrapperLogFile:
        
        for strLogLine in listLogLines:
            listLogLine = strLogLine.split(" ")
            strIPAddress = listLogLine[0]
            strReturnCode = listLogLine[8]
            strIPReturnCode = f"{strIPAddress} - {strReturnCode}"
            if strReturnCode >= '400':
                print(strIPReturnCode)
                if strReturnCode >= '500':
                    wrapperLogFile.write(f"{strIPReturnCode}\n")
else:
    print("Program has ended")