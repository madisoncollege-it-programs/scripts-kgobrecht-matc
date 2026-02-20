#!/usr/bin/env python3
"""
Author: Keaton Gobrecht
Email: kgobrecht@madisoncollege.edu
Description: <Semester long script which analyzes an Apache web log to determine if the highest-hitting IP address is a current threat.>
"""

#Multiple apache log lines. will be replaced
strLogLines = '''111.222.333.123 HOME - [01/Feb/1998:01:08:39 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 198 "http://www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)"
111.222.333.124 HOME - [01/Feb/1998:01:08:46 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 28083 "http://www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)"
111.222.333.125 AWAY - [01/Feb/1998:01:08:53 -0800] "GET /bannerad/ad7.gif HTTP/1.0" 401 9332 "http://www.referrer.com/bannerad/ba_ad.htm" "Mozilla/4.01 (Macintosh; I; PPC)"
111.222.333.126 AWAY - [01/Feb/1998:01:09:14 -0800] "GET /bannerad/click.htm HTTP/1.0" 501 207 "http://www.referrer.com/bannerad/menu.htm" "Mozilla/4.01 (Macintosh; I; PPC)"'''

listLogLines = strLogLines.split('\n')

for strLogLine in listLogLines:
    listLogLine = strLogLine.split(" ")      
    print(f"log request from: {listLogLine[0]:*^22}")
    print(f"return Code: {listLogLine[8]}")