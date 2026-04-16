import dns.resolver

def dnsEnum(domain):
    try:
        print(f"Getting DNS Information for {domain}")
        for a in dns.resolver.resolve(domain, 'A'):
            if a: print(f"Results: {a.to_text()}")
            else: continue
    except Exception as e:
        print(f"Unable to Resolve DNS Information: {e}")


dnsEnum("cityinthe.cloud")