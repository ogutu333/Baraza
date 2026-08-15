import requests
import json
import whois

SHODAN_API_KEY = "your_shodan_api_key_here"  # Replace with your own Shodan API key

"""
OSINT Script

This script gathers WHOIS information and Shodan data
to perform basic OSINT on a domain.

Usage:
    python OSINT_final.py
"""

def get_whois_info(domain):
    """Fetches WHOIS information for a given domain."""
    try:
        w = whois.whois(domain)
        return w.text
    except Exception as e:
        return f"Error retrieving WHOIS data: {e}"

def get_shodan_info(domain):
    """Fetches Shodan information for a given domain."""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        url = f"https://api.shodan.io/dns/resolve?hostnames={domain}&key={SHODAN_API_KEY}"
        response = requests.get(url, headers=headers)
        ip = response.json().get(domain)

        if ip:
            shodan_url = f"https://api.shodan.io/shodan/host/{ip}?key={SHODAN_API_KEY}"
            shodan_response = requests.get(shodan_url, headers=headers)
            return json.dumps(shodan_response.json(), indent=4)
        else:
            return "No IP found for this domain."

    except Exception as e:
        return f"Error retrieving Shodan data: {e}"

def main():
    """Main function to collect OSINT information on a domain."""
    domain = input("Enter the domain name to investigate: ")

    # Retrieve WHOIS data
    whois_data = get_whois_info(domain)
    print("\n[WHOIS Information]:")
    print(whois_data)

    # Retrieve Shodan data
    shodan_data = get_shodan_info(domain)
    print("\n[Shodan Information]:")
    print(shodan_data)

    # Store data in a dictionary
    osint_results = {
        "WHOIS": whois_data,
        "Shodan": shodan_data
    }

    # Save results to a JSON file
    with open(f"{domain}_osint_report.json", "w") as outfile:
        json.dump(osint_results, outfile, indent=4)

    print(f"\nOSINT report saved to {domain}_osint_report.json")

if __name__ == "__main__":
    main()