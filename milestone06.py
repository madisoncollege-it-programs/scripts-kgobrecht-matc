#!/usr/bin/env python3
"""
Author: Keaton Gobrecht
Email: kgobrecht@madisoncollege.edu
Description: <milestone06 wu06>
"""

import sys

listofYs = ['y', 'yep', 'yup', 'yeah']

if len(sys.argv) > 1:
    strContinue = sys.argv[1].lower
else:
    strContinue = input("Would you like to continue? (y/n)\n>>>>").lower
    
    if strContinue in listofYs:
        
        with open("06.access.log", "r") as wrapperLogFile:
            strLoglines = wrapperLogFile.read()
            
        listLogLines = strLoglines.split('\n')
        
        with open("milestone06analysis.txt", "w") as wrapperLogFile:
            
            for strLogLine in listLogLines:
                listLogLine = listLogLines.split(" ")
                strIPAddress = listLogLine[0]
                strReturnCode = listLogLine[8]
                strIPReturnCode = f"{strIPAddress} - {strReturnCode}"
                if strReturnCode >= '400':
                    print(strIPReturnCode)
                    if strReturnCode >='500':
                        wrapperLogFile.write(f"{strIPReturnCode}\n") 
                    else: 
                        print("Program has ended")

    
            