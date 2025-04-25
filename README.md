# DNS Analysis Tool 🔍

A Python-based tool for analyzing DNS configurations and detecting potential security risks.



## Features ✨
- Comprehensive DNS record analysis (A, AAAA, MX, CNAME, NS, TXT, SOA)
- Subdomain takeover vulnerability detection
- DNS configuration comparison between domains
- PDF/HTML report generation
- DNSSEC validation check
- SPF record verification

## Installation ⚙️

**Prerequisites:**
- Python 3.8+
- pip

**Steps:**
```bash
git clone [https://github.com/yourusername/dns-analysis-tool.git](https://github.com/fazelucq1/DNS-Analysis-Tool.git)
cd dns-analysis-tool
pip install -r requirements.txt
python setup.py install
```

## Usage 🚀

**Basic analysis:**
```bash
dnsanalyze example.com
```

**Generate HTML report:**
```bash
dnsanalyze example.com -f html -o report.html
```

**Compare two domains:**
```bash
dnsanalyze example.com -c example.org -o comparison.pdf
```

**Verbose output:**
```bash
dnsanalyze example.com -v
```

## Command Options 📋
| Option | Description |
|--------|-------------|
| `-o`, `--output` | Output file path |
| `-f`, `--format` | Report format (html/pdf) |
| `-c`, `--compare` | Domain to compare with |
| `-v`, `--verbose` | Show detailed analysis |

## Development 🛠️
1. Fork the repository
2. Create a feature branch
3. Submit a PR

Run tests:
```bash
pytest tests/
```

## Contributing 🤝
- Add new DNS record checks
- Improve report templates
- Add more vulnerability patterns
- Implement API integrations

## License 📄
MIT License - see [LICENSE](LICENSE) for details

---

This complete structure includes:
- Advanced DNS record management
- Reporting system with HTML/PDF templates
- Domain comparison functionality
- Unit tests
- Setup script via `setup.py`
- Full documentation in the README
- Error handling
- Basic vulnerability detection

To fully complete the project (100%), it would be necessary to:
1. Implement real HTTP checks for subdomain takeover
2. Add more templates for PDF reports
3. Implement caching for DNS queries
4. Add support for multiple nameservers
5. Implement full DNSSEC checking
