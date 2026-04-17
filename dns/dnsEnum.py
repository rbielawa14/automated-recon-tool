import dns.resolver

def dnsEnum(domain):
    print(f"Getting DNS Information for {domain}")
    try:
        for a in dns.resolver.resolve(domain, 'A'): 
            print("A Record: ", a.to_text())
    except Exception as e:
        print(f"Unable to Resolve DNS Information: {e}")

    try:
        for ns in dns.resolver.resolve(domain, 'NS'):
            print("NS Record: ", ns.to_text())
    except Exception as e:
        print(f"Unable to Resolve DNS Information: {e}")

    try:
        for mx in dns.resolver.resolve(domain, 'MX'):
            print("MX Record: ", mx.to_text())
    except Exception as e:
        print(f"Unable to Resolve DNS Information: {e}")