#!/usr/bin/env python3
"""
Author: Keaton Gobrecht
Description: working milestone 7. Week7
"""

import sys

def parselogEntry(inStrLogLine):
    listLogLine = inStrLogLine.split(" ")
    outStrIpAddress = listLogLine[0]
    outStrReturnCode = listLogLine[8]
    return outStrIpAddress, outStrReturnCode

def main():
    listYesOptions = ["y", "yes", "yep", "yup", "yeah"]

    if len(sys.argv) > 1:
        strUserAnswer = sys.argv[1].lower()
    else:
        strUserAnswer = input("Would you like to continue? (y/n) ").lower()

    if strUserAnswer in listYesOptions:
        with open("06_CP-Access.log", "r") as wrapperLogFile:
            strLogLines = wrapperLogFile.read()

        listLogLines = strLogLines.split('\n')
        
        dictLogSummary ={}
        
        for strLogLine in listLogLines:
            
            strIPAddress, strIPReturnCode = parselogEntry(strLogLine)
            strIPReturnCode = f"{strIPAddress} - {strIPReturnCode}"
            if strIPReturnCode >= '400':
                print(strIPReturnCode)
                
            if strIPAddress in dictLogSummary:
                dictLogSummary[strIPAddress] += 1
                
            else:
                dictLogSummary[strIPAddress] = 1

        with open("milestone07analysis.csv", "w") as wrapperLogFile:
            wrapperLogFile.write("IP.error\n")
            for strKeyIP, intValueCount in dictLogSummary.items():
                if intValueCount >= 5:
                    wrapperLogFile.write(f"{strKeyIP}, {intValueCount}\n")
                    
if __name__ == "__main__":
    main()
            