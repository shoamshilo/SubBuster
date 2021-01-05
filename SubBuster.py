#!/usr/bin/python3
import sys , requests , socket
from os import path

Banner = """Usage: 
-d - Spesify the base domain.
-w - Path to the wordlist. If the flag is not 
     set SubBuster will use its own wordlist.
-o - Spesify a output file.
-f - Spesify a list of domains.
-p - Spesify a port 80 or 443.
-v - Verbos output.
-I - Toggle hostname IP resolve.
help - Help menu.

---SubBuster v0.2---
Created By: @shoamshilo 2020"""

verbos = False
ip = False
ListFile = ""
outFile = "" 
ports = ""
domain = ""
wordlist = ""
Domains = []
mark = '[+] '

def StartUp():        
    global verbos
    global ip
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
        if argv == '-I':
            ip = True
        if argv == '-v':
            verbos = True
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
                http = f"http://{line.strip()}.{domain}"
                https = f"https://{line.strip()}.{domain}"
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
                if verbos:
                    print(mark + Domains[len(Domains)-1])
                line = File.readline()  

def listFile():
    global domain
    try:
        with open(ListFile, 'r') as listfile:
            domain = listfile.readline().strip()
            while domain:
                print(mark + f"Busting {domain}:")
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

def ip_resolve():
        i=0
        for url in Domains:
           s = url.split('/')
           url = f"{url} : {socket.gethostbyname(s[2])}"
           Domains[i] = url
           i+=1

def printDomains():
    if ip:
        ip_resolve()
    print(mark +  f"Found {str(len(Domains))} sub-domains:")
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
        if outFile:
            OutPut()
        printDomains()
        if outFile:
            OutPut()
        sys.exit()
    BrutForce()
    printDomains()
    if outFile:
        OutPut()