import sys
import requests
from os import path



Banner = """
Usage: 
-d - spesify the base domain
-w - Path to the wordlist. if the flag is not set 
     SubBuster will use its own wordlist.
help - Help menu
"""
    

File = "" 
domain = ""
wordlist = ""
Domains = []
mark = '[+] '


def StartUp():        
    global domain
    global wordlist
    i = 0 

    print(mark + 'Created By: @shoamshilo 2020 \n')

    if len(sys.argv) == 1:
        print(mark + "For help type - SubBuster.py help")
        sys.exit()
    for argv in sys.argv:
        if argv == "-d":
            domain = sys.argv[i + 1]
        if argv == "-w":
            wordlist = sys.argv[i + 1]
        if argv == "help":
            print(Banner)
            sys.exit()
        i+=1
    if wordlist == "":
        wordlist = 'wordlist.txt'


def BrutForce():
    global Domains
    if path.exists(wordlist):
        with open(wordlist) as File:
            line = File.readline()
            while line:
                try:
                    url = "http://" + line.strip() + "." +  domain
                    r = requests.get(url)
                    if r.status_code:
                        Domains.insert(len(Domains) , url)
                except requests.exceptions.ConnectionError:   
                    pass
                line = File.readline()
    else:
        print(mark + "File not found error:")
        print(mark + wordlist + "dosent exists")     

def printDomains():
    print(mark +  "The domain " + domain + " has " + str(len(Domains)) + " sub-domains")
    for url in Domains:
        print(mark + url)

   
if __name__ == '__main__':
    StartUp()
    BrutForce()
    printDomains()



