"""
==========================================================
README
==========================================================

Automated Google Dorking Script

Purpose:
This script automates Google dorking searches for security
research and reconnaissance.

Features:
- Generates predefined Google dorking queries.
- Allows users to add custom queries.
- Sends search requests to Google.
- Parses search results.
- Saves results to a text file.
- Includes basic error handling.
- Supports resuming searches by skipping completed queries.

Requirements:
- requests
- beautifulsoup4

Install dependencies:
pip install requests beautifulsoup4

Run:
python dork_final.py

==========================================================
"""

import os
import time
import requests
from bs4 import BeautifulSoup

# Define user-agent to mimic a real browser
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/91.0.4472.124 Safari/537.36"
    )
}

# Base Google search URL
GOOGLE_SEARCH_URL = "https://www.google.com/search?q="

# --------------------------------------------------------
# Step 2: Functions
# --------------------------------------------------------

def generate_dork_queries():
    """Generate Google dorking queries for security research."""
    queries = [
        "inurl:login",
        "filetype:pdf OR filetype:doc",
        "intitle:index.of mysql"
    ]
    return queries

def send_search_request(query):
    """Send a request to Google Search."""
    try:
        search_url = GOOGLE_SEARCH_URL + query
        response = requests.get(search_url, headers=HEADERS)

        if response.status_code == 200:
            return response.text
        else:
            print(f"Error: Unable to fetch results for {query}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def parse_search_results(html):
    """Extract search result URLs from Google's search response."""
    soup = BeautifulSoup(html, "html.parser")
    results = []

    for link in soup.find_all("a"):
        href = link.get("href")
        if href and "http" in href:
            results.append(href)

    return results

# --------------------------------------------------------
# Step 3: Google Search Requests
# --------------------------------------------------------

def perform_dorking():
    """Perform Google dorking using predefined and user queries."""

    queries = generate_dork_queries()

    custom_query = input(
        "Enter an additional Google dork query (or press Enter to skip): "
    ).strip()

    if custom_query:
        queries.append(custom_query)

    completed_queries = set()

    if os.path.exists("dorking_results.txt"):
        with open("dorking_results.txt", "r") as file:
            for line in file:
                if line.startswith("Results for:"):
                    completed_queries.add(
                        line.replace("Results for:", "").strip()
                    )

    all_results = {}

    for query in queries:

        if query in completed_queries:
            print(f"Skipping completed query: {query}")
            continue

        print(f"Searching: {query}")

        html = send_search_request(query)

        if html:
            results = parse_search_results(html)
            all_results[query] = results

        time.sleep(2)

    return all_results

# --------------------------------------------------------
# Step 4: Save Results
# --------------------------------------------------------

def save_results(results):
    """Save search results to a text file."""

    with open("dorking_results.txt", "a") as file:

        for query, urls in results.items():

            file.write(f"Results for: {query}\n")

            for url in urls:
                file.write(f"{url}\n")

            file.write("\n")

    print("Results saved to dorking_results.txt")

# --------------------------------------------------------
# Main Function
# --------------------------------------------------------

def main():
    print("Welcome to the Automated Google Dorking Script!")

    results = perform_dorking()

    if results:
        save_results(results)
    else:
        print("No results found.")

if __name__ == "__main__":
    main()