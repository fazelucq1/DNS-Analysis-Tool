VULNERABLE_SERVICES = {
    'AWS S3': ['s3.amazonaws.com', 'amazonaws.com'],
    'GitHub Pages': ['github.io', 'github.map.fastly.net'],
    'Heroku': ['herokuapp.com', 'herokudns.com'],
    'Firebase': ['firebaseapp.com', 'web.app']
}

def analyze_dns(records):
    analysis = {}

    analysis['mx_records'] = bool(records.get('MX'))
    analysis['dnssec'] = 'DNSKEY' in records
    analysis['spf'] = any('v=spf1' in txt for txt in records.get('TXT', []))
    

    cname_risks = []
    for cname in records.get('CNAME', []):
        for service, domains in VULNERABLE_SERVICES.items():
            if any(domain in cname for domain in domains):
                cname_risks.append(f"Potential {service} subdomain takeover: {cname}")
    analysis['cname_risks'] = cname_risks
    

    analysis['ns_count'] = len(records.get('NS', []))
    if analysis['ns_count'] < 2:
        analysis['ns_warning'] = "Less than 2 NS records detected"
    
    return analysis

def check_subdomain_takeover(domain):
    risks = []

    cnames = [
        "s3-website-us-east-1.amazonaws.com",
        "herokuapp.com",
        "azurewebsites.net"
    ]
    
    for cname in cnames:
        if cname in domain:
            risks.append(f"Potential subdomain takeover vulnerability detected for {cname}")
    
    return risks
