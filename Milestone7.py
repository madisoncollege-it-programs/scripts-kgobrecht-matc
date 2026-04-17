#!/usr/bin/env python3

"""
Author: Keaton Gobrecht
Description: working milestone 7. Week7
"""

import sys

listYesOptions = ["y", "yes", "yep", "yup", "yeah"]

if len(sys.argv) > 1:
    strUserAnswer = sys.argv[1].lower()
else:
    strUserAnswer = input("Would you like to continue? (y/n) ").lower()

if strUserAnswer in listYesOptions:
    dictLogSummary = {}
    
    with open("06_CP-Access.log", "r") as wrapperLogFile:
        strLogLines = wrapperLogFile.read()

    listLogLines = strLogLines.split('\n')
    
    for strLogLine in listLogLines:
        listLogLine = strLogLine.split(" ")
        if len(listLogLine) > 8:
            strIPAddress = listLogLine[0]
            strReturnCode = listLogLine[8]
            strIPReturnCode = f"{strIPAddress} - {strReturnCode}"
            
            if int(strReturnCode) >= 400:
                print(strIPReturnCode)
                
            if strIPAddress in dictLogSummary:
                dictLogSummary[strIPAddress] +=1
            else:
                dictLogSummary[strIPAddress] =1 

    with open("milestone07analysis.csv", "w") as wrapperLogFile:
        wrapperLogFile.write("IP,hits\n")
        
        for strIPAddress in dictLogSummary:
            if dictLogSummary[strIPAddress] >=5:
                wrapperLogFile.write(f"{strIPAddress},{dictLogSummary[strIPAddress]}\n")