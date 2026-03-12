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

    
dictLogSummary = {}

for strLogLine in listLogLines:
        listLogLine = strLogLine.split(" ")
        strIPAddress = listLogLine[0]
        strIPReturnCode = listLogLine[8]
        strIPReturnCode = f"{strIPAddress} - {strIPReturnCode}"
        if strIPReturnCode >= '400':
            print(strIPReturnCode)
        if strIPAddress in dictLogSummary:
            dictLogSummary[strIPAddress] += 1
        else:
            dictLogSummary[strIPAddress] = 1
    
with open("milestone07analysis.csv","w") as wrapperIPCountFile:
          wrapperIPCountFile.write(f"IP,errors\n")
          for strKeyIP, intValueCount in dictLogSummary.items():
            if intValueCount >= 5:
                wrapperIPCountFile.write(f"{strKeyIP},{intValueCount}\n")