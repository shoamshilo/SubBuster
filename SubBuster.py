#!/usr/bin/env python

import sys , requests , socket , re , argparse 
import urllib.parse as urlparse
from os import path

quiet = False
verbose = False
ip = False
api_key = ""
ListFile = ""
outFile = "" 
ports = ""
domain = ""
wordlist = ""
Emails = []
Domains = []
mark = '[+] '

def StartUp():
    global quiet
    global api_key        
    global verbose
    global ip
    global domain
    global outFile
    global wordlist
    global ListFile
    global ports
    
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,epilog='Example: python ' + sys.argv[0] + " -d google.com -o out.txt" + '\n\n---SubBuster v0.4---\nCreated By: @shoamshilo 2020 ',
    description='''SubBuster is a sub-domain discovery tool that uses a custom made wordlist to detect sub-domains.\nThis tool can assist penetration tester or OSINT investigators in determining a corporation sub-domains.\nit allowsfor both active and passive scanning of a domain.''')
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-d' , action='store', dest='domain' , help='Specify the base domain.')
    parser.add_argument('-w' , action='store', dest='wordlist' , help="Path to the wordlist. If the flag is not set SubBuster will use its wordlist.")
    parser.add_argument('-q', action='store_true', default=False, dest='quiet' , help='Toggle quiet mode.')
    parser.add_argument('-o' , action='store', dest='outFile', help='Specify an output file.')
    parser.add_argument('-f' , action='store', dest='ListFile' ,help='Specify a list of domains.')
    parser.add_argument('-p' , action='store', dest='ports' , help='Specify a port 80 or 443.')
    parser.add_argument('-v' , action='store_true', default=False, dest='verbose' , help=' Verbose output.')
    parser.add_argument('-E' , action='store', dest='api_key' , help='Toggle email searching with hunter.io. Requires an API key.')
    parser.add_argument('-I' , action='store_true', default=False, dest='ip' , help='Toggle hostname IP resolve')
    parser.add_argument('--version' ,  action='version',dest='v0.4')

    args =  parser.parse_args()

    quiet = args.quiet
    verbose = args.verbose
    ip = args.ip
    api_key = args.api_key
    ListFile = args.ListFile
    outFile = args.outFile 
    ports = args.ports
    domain = args.domain
    wordlist = args.wordlist

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
                        if url_check(http) and not inDomains(http):
                            Domains.append(http)
                    if '443' in port:
                        if url_check(https) and not inDomains(https):
                            Domains.append(https)
                elif url_check(https) and not inDomains(https):
                    Domains.append(https)            
                else:
                    if url_check(http) and not inDomains(http):
                        Domains.append(http)
                if verbose:
                    print(mark + Domains[len(Domains)-1]) 
                line = File.readline()  

def qBruteForce():
    page_no = 100
    baseurl = f"https://google.com/search?q={domain}&btnG=Search&hl=en-US&biw=&bih=&gbv=1&start={page_no}&filter=0"
    resp = requests.get(baseurl)
    extractdomains(responsehandler(resp))

def extractdomains(resp):
    global Domains
    list = []
    regex = re.compile(r'(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+')
    try:
        list = regex.findall(resp)
        for link in list:
            if link.startswith('http'):
                link = 'https://' + urlparse.urlparse(link).netloc
                if link.endswith(domain) and not inDomains(link):
                    Domains.append(link)
                    if verbose:
                        print(mark + link)
    except:
        pass

def responsehandler(response):
    if response is None:
        return 0
    return response.text if hasattr(response, "text") else response.connect

def inDomains(domain):
    for url in Domains:
        if url == domain:
            return True
    return False

def listFile():
    global domain
    try:
        with open(ListFile, 'r') as listfile:
            domain = listfile.readline().strip()
            while domain:
                print(mark + f"Busting {domain}:")
                if quiet:
                    qBruteForce()
                else:
                    BrutForce()
                domain = listfile.readline()
    except FileNotFoundError:
        print(mark +  """There is an error with your domain file. 
    it is either not found or it doesn't exists.""")
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

def hunter():
    global Emails
    url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={api_key}"
    r = requests.get(url)
    response = r.json()
    for email in response['data']['emails']:
        Emails.append("Email: " + str(email['value']))

def printDomains():
    if ip:
        ip_resolve()
    print(mark +  f"Found {str(len(Domains))} sub-domains:")
    for url in Domains:
        print(mark + url)
    for email in Emails:
        print(mark + email)

def OutPut():
    with open(outFile , 'w') as out:
        for url in Domains:
            out.writelines(url + '\n')
        out.writelines('Email for the domain'+ '\n')
        for email in Emails:
            out.writelines(email + '\n')

def ErrorCheck():
    global wordlist
    if not wordlist:
        print(mark + "You haven't specified a wordlist. Useing SubBusters wordlist.")
        wordlist = "wordlist.txt"
    if not path.exists(wordlist):
        print(mark + """There is an error with your wordlist. 
    it is either not found or it doesn't exists.""")
        sys.exit()    
    if not domain:
        if ListFile:
            return True
        print(mark + "You haven't specified a domain.")
        sys.exit()
    return True
   
if __name__ == '__main__':
    StartUp()
    if quiet:
        qBruteForce()
    elif not quiet:
        BrutForce()
    if ListFile:
        listFile()
    printDomains()
    if outFile:
        OutPut()