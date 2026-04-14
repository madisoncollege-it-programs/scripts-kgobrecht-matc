#!/usr/bin/env python3
"""
Author: Keaton Gobrecht
Email: kgobrecht@madisoncollege.edu
Description: working milestone 10. Week 10
"""

import sys, subprocess

def ipAddressCount(inApacheLogFileName):
    strLinuxCmd = f"cat {inApacheLogFileName} | cut -d ' ' -f1 | sort -n | uniq -c | sort -n | tail -n5"
    completedProcess = subprocess.run(strLinuxCmd, stdout=subprocess.PIPE, shell=True, text=True)
    return completedProcess.stdout

# Not used in this script. Saving as a utility for importing to other scripts._
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

        strLinuxCmdResults = ipAddressCount("06_CP-Access.log")
        print(strLinuxCmdResults)
        with open("milestone10analysis.txt", "w") as wrapperIPCountFile:
            wrapperIPCountFile.write(strLinuxCmdResults)

if __name__== "__main__":
    main()
