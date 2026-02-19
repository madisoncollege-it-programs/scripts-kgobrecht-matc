#!/usr/bin/env python3
"""
Author: Keaton Gobrecht
Email: kgobrecht@madisoncollege.edu
Description: <Semester long script which analyzes an Apache web log to determine if the highest-hitting IP address is a current threat.>
"""
print("Keaton Gobrecht")

strUserInputName = input("What is your name?\n>>>> ")
print()
print("Welcome, " , {strUserInputName} , "!")
strLogLine = '111.222.333.123 HOME - [01/Feb/1998:01:08:39 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 198 "http://www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)"'
listLogLine = strLogLine.split()
print(f"log request from:  {listLogLine [0]:*^22s}")
print(f"Return Code: {listLogLine[8]}")