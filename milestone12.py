#!/usr/bin/env python3
"""
Author: Keaton Gobrecht
Description: working milestone 11. Week11
"""

import subprocess
import argparse
import requests
import bs4

def ipAddressCount(inApacheLogFileName):
    strCommand = f"cat {inApacheLogFileName} | cut -d ' ' -f1 | sort -n |uniq -c | sort -n | tail -n5"
    objProcess = subprocess.run(strCommand, shell=True, capture_output=True, text=True)
    return objProcess.stdout

def ipLookup(inIPAddress):
    strURL = f"http://py.land/geo?host={inIPAddress}"
    print(strURL)
    
    objResponse = requests.get(strURL)
    return objResponse.text

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
                
        listTopIPs = strResults.strip().split("\n")
        strHighestLine = listTopIPs[-1]
        listHighestLineParts = strHighestLine.split()
        strHighestIP = listHighestLineParts[1]
        
        htmlResponse = ipLookup(strHighestIP)
        
        myHTML = bs4.BeautifulSoup(htmlResponse, features="html.parser")
        listRawIPInfo = myHTML.find_all("dd",class_="col-8 text-monospace")
        
        print(f"City: {listRawIPInfo[0].text}")
        print(f"Region: {listRawIPInfo[1].text}")
        print(f"Country: {listRawIPInfo[2].text}")
        print(f"Continent {listRawIPInfo[3].text}")
        print(f"Coordinates: {listRawIPInfo[4].text}")
        print(f"IP Address: {listRawIPInfo[5].text}")
        print(f"Host Name: {listRawIPInfo[6].text}")
        print(f"Provider: {listRawIPInfo[7].text}")
        print(f"ASN: {listRawIPInfo[8].text}")
        
if __name__ == "__main__":
    main()
            