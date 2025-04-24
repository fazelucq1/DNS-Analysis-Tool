import pytest
from dns_analyzer.dns_queries import get_dns_records
from dns_analyzer.analysis import analyze_dns

def test_dns_records(monkeypatch):
    def mock_resolve(query, rtype):
        class MockAnswer:
            def __init__(self, records):
                self.records = records
            def __iter__(self):
                return iter(self.records)
        class MockRecord:
            def to_text(self):
                return "mock.record.com"
        
        if rtype == 'A':
            return MockAnswer([MockRecord(), MockRecord()])
        raise dns.resolver.NoAnswer
    
    monkeypatch.setattr(dns.resolver.Resolver, 'resolve', mock_resolve)
    
    records = get_dns_records('test.com')
    assert 'A' in records
    assert len(records['A']) == 2

def test_analysis():
    sample_records = {
        'MX': ['10 mail.example.com'],
        'CNAME': ['example.s3.amazonaws.com'],
        'TXT': ['v=spf1 include:_spf.example.com ~all']
    }
    analysis = analyze_dns(sample_records)
    
    assert analysis['mx_records'] is True
    assert 's3.amazonaws.com' in analysis['cname_risks'][0]
    assert analysis['spf'] is True
