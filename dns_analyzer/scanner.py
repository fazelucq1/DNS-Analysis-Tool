from typing import Dict, List
import dns.resolver
from typing import Dict, List

class DNSScanner:
    RECORD_TYPES = [
        'A', 'AAAA', 'MX', 'CNAME', 'NS', 'TXT',
        'SOA', 'PTR', 'SRV', 'DNSKEY', 'DS'
    ]

    def __init__(self, nameservers: List[str] = None):
        self.resolver = dns.resolver.Resolver()
        if nameservers:
            self.resolver.nameservers = nameservers
        self.resolver.timeout = 3
        self.resolver.lifetime = 5

    def get_records(self, domain: str) -> Dict:
        results = {}
        for record_type in self.RECORD_TYPES:
            try:
                answers = self.resolver.resolve(domain, record_type)
                results[record_type] = [str(r) for r in answers]
            except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
                continue
            except dns.exception.DNSException as e:
                results[record_type] = str(e)
        return results
