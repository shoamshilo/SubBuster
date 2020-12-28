import sys
import requests
from time import sleep

File = "" 
domain = ""
wordlist = ""


def StartUp():        
    global domain
    global wordlist

    i=0
    for argv in sys.argv:
        if argv == "-d":
            domain = sys.argv[i + 1]
        if argv == "-w":
            wordlist = sys.argv[i + 1]
        i+=1
    
def BrutForce():
    with open(wordlist) as File:
        line = File.readline()
        while line:
            try:
                url = "http://" + line.strip() + "." +  domain
                r = requests.get(url)
                if r.status_code:
                    print(line + " is a sub domain of " +  domain)
            except requests.exceptions.ConnectionError:   
                print(line + " is not sub domain of " +  domain)
            line = File.readline()
            

   

    
    
StartUp()
BrutForce()


