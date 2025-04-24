import dns.resolver
import dns.exception

def get_dns_records(domain):
    records = {}
    record_types = ['A', 'AAAA', 'MX', 'CNAME', 'NS', 'TXT', 'SOA', 'DNSKEY']
    
    resolver = dns.resolver.Resolver()
    resolver.timeout = 5
    resolver.lifetime = 5
    
    for rt in record_types:
        try:
            answer = resolver.resolve(domain, rt)
            records[rt] = [r.to_text() for r in answer]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            continue
        except dns.exception.DNSException as e:
            raise Exception(f"DNS query failed: {str(e)}")
    
    if not any(records.values()):
        raise ValueError(f"Domain {domain} does not exist or has no DNS records")
    
    return records
