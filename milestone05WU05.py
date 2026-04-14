#!/usr/bin/env python3
"""
Author: Keaton Gobrecht
Description: working milestone 5. Week5 
"""
with open("05_CP-Access.log", "r") as wrapperLogFile:
    strLogLines = wrapperLogFile.read()

listLogLines = strLogLines.split('\n')

with open("milestone05analysis.txt", "w") as wrapperLogFile:
    
    for strLogLine in listLogLines:
        listLogLine = strLogLine.split(" ")
        strIPReturnCode = f"{listLogLine[0]} - {listLogLine[8]}"
        print(strIPReturnCode)
        wrapperLogFile.write(f"{strIPReturnCode}\n")
