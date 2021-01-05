# SubBuster
SubBuster is a sub-domain discovery tool that uses a custom made wordlist to detect sub-domains.
This tool can assist penetration tester or OSINT investigators in determining a corporation sub-domains.
 

## Table of contents
* [General info](#general-info)
* [Installation](#installation)
* [Features](#features)
* [Status](#status)
* [Credits](#credits)
* [Contact](#contact)

## General info


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
Usage: 
-d - Specify the base domain.
-w - Path to the wordlist. If the flag is not 
     set SubBuster will use its wordlist.
-o - Specify an output file.
-f - Specify a list of domains.
-p - Specify a port 80 or 443.
-v - Verbos output. 
-I - Toggle hostname IP resolve.
help - Help menu.
```
## Status
The project is in progress. planning on adding more features.

## Credits
[Bitquark](https://github.com/bitquark) - SubBusters wordlist is based on his project.


## Contact
Created by [@shoamshilo](https://github.com/shoamshilo) - feel free to contact me!
 
