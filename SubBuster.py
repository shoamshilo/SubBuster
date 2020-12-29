import sys
import requests
from os import path




Banner = """Usage: 
-d - spesify the base domain.
-w - Path to the wordlist. 
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
                try:
                    url = "http://" + line.strip() + "." +  domain
                    r = requests.get(url)
                    if r.status_code:
                        Domains.insert(len(Domains) ,url)
                except requests.exceptions.ConnectionError:   
                    pass
                line = File.readline()  
    if outFile:
        OutPut()
    

def printDomains():
    print(mark +  "Found " + str(len(Domains)) + " Sub-Domains")
    for url in Domains:
        print(mark + url)

def OutPut():
    with open(outFile , 'w') as out:
        for url in Domains:
            out.writelines(url + '\n')

def ErrorCheck():
    if not wordlist:
        print(mark + "You havent specified a wordlist.")
        sys.exit()
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
    


