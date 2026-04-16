import argparse

def main():
    parser = argparse.ArgumentParser(description="Welcome to ART - An automated, streamlined, recon tool")
    parser.add_argument("--domain", help="Enter the domain to parse.", required=True)
    args = parser.parse_args()
    target = args.domain

    print(f"Running ART On: {target}")
    print("WHOIS DATA:")
    print("-------------------------------")
    getWHOISdata(target)

if __name__ == "__main__":
    main()