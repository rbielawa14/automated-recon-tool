
from httpheader.httpanalysis import get_http_headers
from portscan.portscan import scan_ports
from whoislk.whoislookup import getWHOISdata
from dnsenm.dnsEnum import dnsEnum

def main(domain):
    print(f"Running ART On: {domain}")
    print("WHOIS DATA:")
    print("-------------------------------")
    getWHOISdata(domain)
    print("-------------------------------")

    print("DNS ENUMERATION:") 
    print("-------------------------------")
    dnsEnum(domain)
    print("-------------------------------")

    print("HTTP ANALYSIS:") 
    print("-------------------------------")
    get_http_headers("https://" + domain)
    print("-------------------------------")

    print("PORT SCANNING:") 
    print("-------------------------------")
    scan_ports(domain)
    print("-------------------------------")

if __name__ == "__main__":
    target = input("Enter the domain: ")
    main(target)