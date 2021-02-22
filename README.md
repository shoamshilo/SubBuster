# SubBuster
SubBuster is a sub-domain discovery tool that uses a custom made wordlist to detect sub-domains.
This tool can assist penetration tester or OSINT investigators in determining a corporation sub-domains. it allows
for both active and passive scanning of a domain

## Table of contents
* [Installation](#installation)
* [Features](#features)
* [Status](#status)
* [Credits](#credits)
* [Contact](#contact)

## Installation
First clone the repository to your local machine:

`git clone https://github.com/shoamshilo/SubBuster`

### Linux
Install the dependencies:

`pip install requests`

change the file permissions:

`chmod +x SubBuster.py`

### Windows
install the dependencies:

`pip install requests`


## Code Examples
Usage:
* Command for the help menu:

``python SubBuster.py help``

* Search the domain google.com for sub-domains:

``python SubBuster.py -d google.com -o out.txt``

## Features
```
usage: SubBuster.py [-h] [-d DOMAIN] [-w WORDLIST] [-q] [-o OUTFILE] [-f LISTFILE] [-p PORTS] [-v] [-E API_KEY] [-I] [--version]

OPTIONS:
  -h, --help   show this help message and exit
  -d DOMAIN    Specify the base domain.
  -w WORDLIST  Path to the wordlist. If the flag is not set SubBuster will use its wordlist.
  -q           Toggle quiet mode.
  -o OUTFILE   Specify an output file.
  -f LISTFILE  Specify a list of domains.
  -p PORTS     Specify a port 80 or 443.
  -v           Verbose output.
  -E API_KEY   Toggle email searching with hunter.io. Requires an API key.
  -I           Toggle hostname IP resolve
  --version    show program's version number and exit

Example: python SubBuster.py -d google.com -o out.txt

---SubBuster v0.3---
Created By: @shoamshilo 2020
```
## Status
The project is in progress. planning on adding more features.

## Credits
[Bitquark](https://github.com/bitquark) - SubBusters wordlist is based on his project.


## Contact
Created by [@shoamshilo](https://github.com/shoamshilo) - feel free to contact me!
 
