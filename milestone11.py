#!/usr/bin/env python3
"""
Author: Keaton Gobrecht
Description: working milestone 11. Week11
"""

import subprocess
import argparse

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
        parser = argparse.ArgumentParser(description="Process Apache log files")
        
        parser.add_argument("-i", "--infilename", required=True, type=str, help="Apache log file to process")
        
        parser.add_argument("-o", "--outfilename", required=False, type=str, help="Output file to write results" )
        
        args = parser.parse_args()
        
        strResults = ipAddressCount(args.infilename)
        
        print(strResults)
        if args.outfilename:
            with open(args.outfilename, "w") as wrapperIpCountFile:
                wrapperIpCountFile.write(strResults)
if __name__ == "__main__":
    main()
            