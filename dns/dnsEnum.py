import dns.resolver

def dnsEnum(domain):
    try:
        print(f"Getting DNS Information for {domain}")
        for a in dns.resolver.resolve(domain, 'A'): 
            print("A Record: ", a.to_text())
        for ns in dns.resolver.resole(domain, 'NS'):
            print("NS Record: ", ns.to_text())
        for MX in dns.resolver.resole(domain, 'MX'):
            print("NS Record: ", ns.to_text())
    except Exception as e:
        print(f"Unable to Resolve DNS Information: {e}")

dnsEnum("www.google.com")