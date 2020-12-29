#!/usr/bin/python3

import sys , httplib2
from os import path

Banner = """Usage: 
-d - spesify the base domain.
-w - Path to the wordlist. If the flag is not 
     set SubBuster will use its own wordlist.
-o - Spesify a output file.
help - Help menu

Created By: @shoamshilo 2020"""
    
outFile = "" 
domain = ""
wordlist = ""
Domains = []
mark = '[+] '

def StartUp():        
    global domain
    global outFile
    global wordlist
    i = 0 

    if len(sys.argv) == 1:
        print(mark + "For help type - SubBuster.py help")
        sys.exit()
    for argv in sys.argv:
        if argv == "-d":
            domain = sys.argv[i + 1]
        if argv == "-w":
            wordlist = sys.argv[i + 1]
        if argv == "-o":
            outFile = sys.argv[i + 1]
        if argv == "help":
            print(Banner)
            sys.exit()
        i+=1

def BrutForce():
    global Domains
    if ErrorCheck():
        print(mark +"Searching Sub Domains")
        with open(wordlist) as File:
            line = File.readline()
            while line:
                http = "http://" + line.strip() + "." +  domain
                https = "https://" + line.strip() + "." +  domain
                if url_check(https):
                    Domains.insert(len(Domains) , https)
                else:
                    if url_check(http):
                        Domains.insert(len(Domains) , http)
                line = File.readline()  
    if outFile:
        OutPut()

def url_check(url):
    h = httplib2.Http()
    try:
        resp, content = h.request(url , 'HEAD')
        if resp.status:
            return True
        else:
            return False
    except httplib2.ServerNotFoundError:
        pass

def printDomains():
    print(mark +  "Found " + str(len(Domains)) + " Sub-Domains:")
    for url in Domains:
        print(mark + url)

def OutPut():
    with open(outFile , 'w') as out:
        for url in Domains:
            out.writelines(url + '\n')

def ErrorCheck():
    global wordlist
    if not wordlist:
        print(mark + "You havent specified a wordlist. Useing SubBusters wordlist.")
        wordlist = "wordlist.txt"
    if not path.exists(wordlist):
        print(mark + """There is an error with your wordlist. 
    it is either not found or it dosent exists.""")
        sys.exit()
    if not domain:
        print(mark + "You havent specified a domain.")
        sys.exit()
    return True
   
if __name__ == '__main__':
    StartUp()
    BrutForce()
    printDomains()