# DNS Analysis Tool 🔍

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python-based DNS analysis tool for security checks and configuration validation.


## Features ✨
- Full DNS record analysis (A, AAAA, MX, CNAME, NS, TXT, SOA)
- Subdomain takeover detection
- Multi-domain comparison
- PDF/HTML report generation
- DNSSEC validation
- SPF record verification
- Vulnerability scanning

## 🛠️ Installation 

### Prerequisites
- Python 3.8 or later
- Git

### Linux/Ubuntu Setup
```bash
# Install python3-venv if not available
sudo apt update && sudo apt install python3.10-venv

# Clone repository
git clone https://github.com/fazelucq1/DNS-Analysis-Tool.git
cd DNS-Analysis-Tool

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -e .
```

### Windows Setup
```bash
# Clone repository
git clone https://github.com/fazelucq1/DNS-Analysis-Tool.git
cd DNS-Analysis-Tool

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -e .
```

### macOS Setup
```bash
# Install Homebrew if not installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Clone repository
git clone https://github.com/fazelucq1/DNS-Analysis-Tool.git
cd DNS-Analysis-Tool

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -e .
```

## 🚀 Usage

Basic DNS analysis:
```bash
dnsanalyze example.com
```

Generate HTML report:
```bash
dnsanalyze example.com -f html -o report.html
```

Compare two domains:
```bash
dnsanalyze example.com -c example.org -o comparison.pdf
```

Verbose mode (detailed output):
```bash
dnsanalyze example.com -v
```

## 📂 Project Structure
```
DNS-Analysis-Tool/
├── dns_analyzer/          # Core application code
├── tests/                 # Unit tests
├── templates/             # Report templates
├── examples/              # Sample reports
├── screenshots/           # Documentation images
├── requirements.txt       # Dependencies
├── setup.py               # Package configuration
└── README.md              # This file
```

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

## 📧 Contact
Luca Crippa - [luca.crippa05@gmail.com](mailto:luca.crippa05@gmail.com)

Project Link: [https://github.com/fazelucq1/DNS-Analysis-Tool](https://github.com/fazelucq1/DNS-Analysis-Tool)
```
