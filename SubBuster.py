import sys
import requests


File = "" 
domain = ""
wordlist = ""
Domains = []

def StartUp():        
    global domain
    global wordlist
    i = 0 

    for argv in sys.argv:
        if argv == "-d":
            domain = sys.argv[i + 1]
        if argv == "-w":
            wordlist = sys.argv[i + 1]
        i+=1




def BrutForce():
    global Domains
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
            

   
if __name__ == '__main__':
    StartUp()
    BrutForce()
    for url in Domains:
        print(url)



