import argparse
import sys
import datetime
from .dns_queries import get_dns_records
from .analysis import analyze_dns, check_subdomain_takeover
from .reporter import generate_report

def compare_domains(domain1, domain2):
    try:
        records1 = get_dns_records(domain1)
        records2 = get_dns_records(domain2)
        
        comparison = {
            'domain1': domain1,
            'domain2': domain2,
            'differences': []
        }
        
        all_keys = set(records1.keys()).union(set(records2.keys()))
        for key in all_keys:
            val1 = records1.get(key, [])
            val2 = records2.get(key, [])
            if val1 != val2:
                comparison['differences'].append({
                    'record_type': key,
                    domain1: val1,
                    domain2: val2
                })
        
        return comparison
    except Exception as e:
        print(f"Error comparing domains: {str(e)}", file=sys.stderr)
        raise

def main():
    parser = argparse.ArgumentParser(description='DNS Analysis Tool')
    parser.add_argument('domain', help='Domain to analyze')
    parser.add_argument('-c', '--compare', help='Domain to compare')
    parser.add_argument('-o', '--output', help='Output file')
    parser.add_argument('-f', '--format', choices=['html', 'pdf'], default='pdf')
    parser.add_argument('-v', '--verbose', action='store_true')
    
    args = parser.parse_args()
    
    try:
        records = get_dns_records(args.domain)
        analysis = analyze_dns(records)
        analysis['generated_at'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        takeover_risk = check_subdomain_takeover(args.domain)
        
        comparison = None
        if args.compare:
            comparison = compare_domains(args.domain, args.compare)
        
        if args.output:
            generate_report(
                args.domain,
                analysis,
                takeover_risk,
                args.format,
                args.output,
                comparison=comparison,
                verbose=args.verbose
            )
        else:
            print(f"=== DNS Analysis for {args.domain} ===")
            print(f"Generated at: {analysis['generated_at']}")
            print("\n".join(f"{k}: {v}" for k, v in analysis.items()))
            if takeover_risk:
                print("\n=== Potential Risks ===")
                print("\n".join(takeover_risk))
            
            if comparison:
                print("\n=== Domain Comparison ===")
                for diff in comparison['differences']:
                    print(f"{diff['record_type']}:")
                    print(f"{args.domain}: {diff[args.domain]}")
                    print(f"{args.compare}: {diff[args.compare]}\n")
                    
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
