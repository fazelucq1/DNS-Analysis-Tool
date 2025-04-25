from .scanner import DNSScanner
from tqdm import tqdm
import concurrent.futures

class SubdomainBruteforcer(DNSScanner):
    def __init__(self, wordlist: str, threads: int = 50):
        super().__init__()
        self.wordlist = wordlist
        self.threads = threads

    def _check_subdomain(self, subdomain: str):
        try:
            self.resolver.resolve(subdomain, 'A')
            return subdomain
        except:
            return None

    def run(self, domain: str) -> List[str]:
        found = []
        with open(self.wordlist, 'r') as f:
            subdomains = [f"{line.strip()}.{domain}" for line in f]
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = {executor.submit(self._check_subdomain, sub): sub for sub in subdomains}
            
            with tqdm(total=len(subdomains), desc="Bruteforcing", unit="sub") as pbar:
                for future in concurrent.futures.as_completed(futures):
                    result = future.result()
                    if result:
                        found.append(result)
                    pbar.update(1)
        
        return found
