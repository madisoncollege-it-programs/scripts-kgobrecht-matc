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
