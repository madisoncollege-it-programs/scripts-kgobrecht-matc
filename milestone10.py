#!/usr/bin/env python3
"""
Author: Keaton Gobrecht
Description: working milestone 10. Week10
"""

import sys
import subprocess


#def parselogEntry(inStrLogLine):
    #listLogLine = inStrLogLine.split(" ")
    #outStrIpAddress = listLogLine[0]
    #outStrReturnCode = listLogLine[8]
    #return outStrIpAddress, outStrReturnCode

def ipAddressCount(inApacheLogFileName):
    strCommand = f"cat {inApacheLogFileName} | cut -d ' ' -f1 | sort -n |uniq -c | sort -n | tail -n5"
    objProcess = subprocess.run(strCommand, shell=True, capture_output=True, text=True)
    return objProcess.stdout

def main():
    listYesOptions = ["y", "yes", "yep", "yup", "yeah"]

    if len(sys.argv) > 1:
        strUserAnswer = sys.argv[1].lower()
    else:
        strUserAnswer = input("Would you like to continue? (y/n) ").lower()

    if strUserAnswer in listYesOptions:
        strResults = ipAddressCount("06_CP-Access.log")
        
        print(strResults)

        with open("milestone10analysis.txt", "w") as wrapperIPCountFile:
            wrapperIPCountFile.write(strResults)
                    
if __name__ == "__main__":
    main()
            