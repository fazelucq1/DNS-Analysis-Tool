import argparse
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from .scanner import DNSScanner
from .bruteforce import SubdomainBruteforcer
import os

def main():
    parser = argparse.ArgumentParser(description="Advanced DNS Scanner")
    parser.add_argument("domain", help="Domain to scan")
    parser.add_argument("-o", "--output", help="Output HTML file")
    parser.add_argument("-w", "--wordlist", help="Wordlist for subdomain bruteforce")
    parser.add_argument("-t", "--threads", type=int, default=50, help="Threads for bruteforce")
    
    args = parser.parse_args()
    
    # Scan DNS Records
    scanner = DNSScanner()
    records = scanner.get_records(args.domain)
    
    # Bruteforce Subdomains
    subdomains = []
    if args.wordlist:
        bruteforcer = SubdomainBruteforcer(args.wordlist, args.threads)
        subdomains = bruteforcer.run(args.domain)
  
    if args.output:
        env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates'))
        template = env.get_template('report.html')
        
        html = template.render(
            domain=args.domain,
            records=records,
            subdomains=subdomains,
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        
        with open(args.output, 'w') as f:
            f.write(html)
        print(f"Report saved to {args.output}")
    else:
        print("\nDNS Records:")
        for record, values in records.items():
            print(f"\n{record}:")
            for value in values:
                print(f"  {value}")
        
        if subdomains:
            print("\nFound Subdomains:")
            for sub in subdomains:
                print(f"  {sub}")

if __name__ == "__main__":
    main()
