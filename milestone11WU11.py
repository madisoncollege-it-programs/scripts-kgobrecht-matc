#!/usr/bin/env python3
"""
Author: Keaton Gobrecht.
Description: milestone 11. Week 11
"""

import subprocess, argparse


def ipAddressCount(inApacheLogFileName):
    strLinuxCmd = f"cat {inApacheLogFileName} | cut -d ' ' -f1 | sort -n | uniq -c | sort -n | tail -n5"
    completedProcess = subprocess.run(strLinuxCmd, stdout=subprocess.PIPE, shell=True, text=True)
    return completedProcess.stdout

    
def main():
    
    parser = argparse.ArgumentParser(description="Supplies input and output filenames")
    parser.add_argument('-i', '--inputfilename', required=True, help="REQUIRED: Apache log file to process.")
    parser.add_argument('-o', '--outputfilename', help='OPTIONAL: The filename to store the top-hitting IPs and their counts.')
    args = parser.parse_args()
     
    strLinuxCmdResults = ipAddressCount(args.inputfilename)
    print(strLinuxCmdResults)
    
    
    if args.outputfilename:
        with open(args.outputfilename, "w") as wrapperIPCountFile:
                wrapperIPCountFile.write(strLinuxCmdResults)

if __name__== "__main__":
    main()
