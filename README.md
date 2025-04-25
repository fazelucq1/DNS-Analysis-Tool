# DNS Analysis Tool 🔍

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Advanced DNS scanner with subdomain bruteforcing and professional reporting.

![image](https://github.com/user-attachments/assets/396f6a43-3445-4109-9637-2e4132b01dce)


## Features
- Full DNS record scanning (like dig)
- Subdomain bruteforce with wordlists
- Professional HTML reports with TailwindCSS
- Multi-threaded scanning
- Clean CLI output

## Install
```bash
git clone https://github.com/fazelucq1/DNS-Analysis-Tool.git
cd DNS-Analysis-Tool
pip install -e .
```

## Usage
Basic scan:
```bash
dnsanalyze example.com
```

Full scan with bruteforce:
```
dnsanalyze example.com -w wordlists/subdomains.txt -o report.html
```

Options:
- `-o/--output`: Save HTML report
- `-w/--wordlist`: Wordlist for subdomain bruteforce
- `-t/--threads`: Threads number (default: 50)

## Sample Wordlist
Included common subdomains in `wordlists/` directory


**Per utilizzare**:
```
# Scan veloce
dnsanalyze example.com

# Scan completo con bruteforce
dnsanalyze example.com -w wordlists/subdomains.txt -o report.html -t 100

# Genera solo report
dnsanalyze example.com -o report.html


