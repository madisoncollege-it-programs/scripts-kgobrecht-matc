#!/usr/bin/env python3

"""
Author: Keaton Gobrecht
Description: working milestone 6. Week6
"""

import sys

listYesOptions = ["y", "yes", "yep", "yup", "yeah"]

if len(sys.argv) > 1:
    strUserAnswer = sys.argv[1].lower()
else:
    strUserAnswer = input("Would you like to continue? (y/n) ").lower()

if strUserAnswer in listYesOptions:
    with open("06_CP-Access.log", "r") as wrapperLogFile:
        strLogLines = wrapperLogFile.read()

    listLogLines = strLogLines.split('\n')

    with open("milestone06analysis.txt", "w") as wrapperLogFile:
        for strLogLine in listLogLines:
            listLogLine = strLogLine.split(" ")

            if len(listLogLine) > 8:
                strIPAddress = listLogLine[0]
                strReturnCode = listLogLine[8]
                strIPReturnCode = f"{strIPAddress} - {strReturnCode}"

                if int(strReturnCode) >= 400:
                    print(strIPReturnCode)

                if int(strReturnCode) >= 500:
                    wrapperLogFile.write(f"{strIPReturnCode}\n")