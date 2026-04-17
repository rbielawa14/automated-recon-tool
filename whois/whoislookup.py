import whois
import socket

def getWHOISdata(domain):
    print("Getting WHOIS Information For: ", domain)
    try:
        target = whois.whois(domain)
        #print(target)
        # Access specific data
        print("WHOIS DATA")
        print("------------------------------")
        print("Name: ", "{}".format(target.name if target.name else "None Found."))
        print("Registrar: ", "{}".format(target.registrar if target.registrar else "None Found."))
        print("Creation Date: ", "{}".format(target.creation_date if target.creation_date else "None Found."))
        print("Expiration Date: ", "{}".format(target.expiration_date if target.expiration_date else "None Found."))
        print("Name Servers: ", "{}".format(target.name_servers if target.name_servers else "None Found."))
    except Exception as e:
        print(f"Error retrieving WHOIS data: {e}")
        return None 