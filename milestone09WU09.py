#!/usr/bin/env python3
"""
Author: Keaton Gobrecht
Description: milestone 9. Week 9
"""
import sys

def parseLogEntry(inStrLogLine):
    listLogLine = inStrLogLine.split(" ")
    outStrIPAddress = listLogLine[0]
    outStrReturnCode = listLogLine[8]
    return outStrIPAddress, outStrReturnCode
    
def main():
    listOfYs = ['y', 'yes', 'yep', 'yup', 'yeah']

    if len(sys.argv) > 1:
        strContinue = sys.argv[1].lower()
    else:
        strContinue = input("Would you like to continue?  (y/n)\n>>>> ").lower()

    if strContinue in listOfYs:

        with open("06_CP-Access.log", "r") as wrapperLogFile:
            strLogLines = wrapperLogFile.read()

        listLogLines = strLogLines.split('\n')
        
        dictLogSummary = {}
        
        for strLogLine in listLogLines:
            #listLogLine = strLogLine.split(" ")
            #strIPAddress = listLogLine[0]
            #strReturnCode = listLogLine[8]
            strIPAddress, strReturnCode = parseLogEntry(strLogLine)
            strIPReturnCode = f"{strIPAddress} - {strReturnCode}"
            if strReturnCode >= '400':
                print(strIPReturnCode)
                
            if strIPAddress in dictLogSummary:
                dictLogSummary[strIPAddress] += 1
            else:
                dictLogSummary[strIPAddress] = 1
        
        with open("milestone07analysis.csv", "w") as wrapperIPCountFile:
            wrapperIPCountFile.write(f"IP,errors\n")
            for strKeyIP, intValueCount in dictLogSummary.items():
                if intValueCount >= 5:
                    wrapperIPCountFile.write(f"{strKeyIP},{intValueCount}\n")

if __name__== "__main__":
    main()
    
