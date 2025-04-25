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

## Installation ⚙️

```bash
git clone https://github.com/fazelucq1/DNS-Analysis-Tool.git
cd DNS-Analysis-Tool
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows
pip install -e .
```

## Usage 🚀

Basic analysis:
```bash
dnsanalyze example.com
```

Generate HTML report:
```bash
dnsanalyze example.com -f html -o report.html
```

Compare domains:
```bash
dnsanalyze example.com -c example.org -o comparison.pdf
```

## Contributing 🤝
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📄
Distributed under the MIT License. See `LICENSE` for more information.

## Contact 📧
Luca - luca.crippa05@gmail.com

```

**Per completare la configurazione:**

1. Crea una cartella `screenshots` per le immagini del README
2. Aggiungi un file `LICENSE` con la licenza MIT
3. Crea una cartella `examples` con report di esempio

Per testare localmente:
```bash
# In ambiente virtuale
dnsanalyze google.com -v
dnsanalyze github.com -f html -o github_report.html
```

