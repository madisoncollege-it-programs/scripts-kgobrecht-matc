#!/usr/bin/env python3
"""
Author: Keaton Gobrecht
Email: kgobrecht@madisoncollege.edu
Description: <Semester long script which analyzes an Apache web log to determine if the highest-hitting IP address is a current threat.>
"""
with open("05.CP.Access.log", "r") as wrapperLogFile:
    strLogLines = wrapperLogFile.read()

listLogLines = strLogLines.split("\n")
    
with open("milestone05analysis.txt", "w") as wrapperLogFile:
     
     for strLogLine in listLogLines:
        listLogLine = strLogLine.split(" ")
        strIPReturnCode = f"{listLogLine[0]} - {listLogLine[8]}"
        print(strIPReturnCode)
        wrapperLogFile.write(f"{strIPReturnCode}\n")

