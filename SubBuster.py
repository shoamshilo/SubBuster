#!/usr/bin/python3
import sys , requests 
from os import path

Banner = """Usage: 
-d - Spesify the base domain.
-w - Path to the wordlist. If the flag is not 
     set SubBuster will use its own wordlist.
-o - Spesify a output file.
-f - Spesify a list of domains.
-p - Spesify a port 80 or 443.
help - Help menu.

---SubBuster v0.1---
Created By: @shoamshilo 2020"""

ListFile = ""
outFile = "" 
ports = ""
domain = ""
wordlist = ""
Domains = []
mark = '[+] '

def StartUp():        
    global domain
    global outFile
    global wordlist
    global ListFile
    global ports
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
        if argv == "-f":
            ListFile = sys.argv[i + 1]
        if argv == '-p':
            ports = sys.argv[i + 1]
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
                if ports:
                    port = Ports()
                    if '80' in port:
                        if url_check(http):
                            Domains.insert(len(Domains) , http) 
                    if '443' in port:
                        if url_check(https):
                            Domains.insert(len(Domains) , https) 
                elif url_check(https):
                    Domains.insert(len(Domains) , https)
                else:
                    if url_check(http):
                        Domains.insert(len(Domains) , http)
                line = File.readline()  

def listFile():
    global domain
    try:
        with open(ListFile, 'r') as listfile:
            domain = listfile.readline().strip()
            while domain:
                print(mark + "Busting " + domain + ':')
                BrutForce()
                domain = listfile.readline()
    except FileNotFoundError:
        print(mark +  """There is an error with your domain file. 
    it is either not found or it dosent exists.""")
        sys.exit()

def url_check(url):
    try:
        r = requests.get(url)
        if r.status_code:
            return True
        return False
    except Exception:
        return False

def Ports():
    return ports.split(',')

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
        if ListFile:
            return True
        print(mark + "You havent specified a domain.")
        sys.exit()
    return True
   
if __name__ == '__main__':
    StartUp()
    if ListFile:
        listFile()
        printDomains()
        if outFile:
            OutPut()
        sys.exit()
    BrutForce()
    if outFile:
        OutPut()
    printDomains()