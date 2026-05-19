import requests
import json

def fetch_threat_intelligence():
    url = 'https://otx.alienvault.com/api/v1/pulses/subscribed'
    headers = {
        'X-OTX-API-KEY': 'YOUR_API_KEY_HERE'  # Optional: only needed for live runs
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def parse_threat_intelligence(data):
    """
    TODO:
    - If no usable results are returned (e.g., None or empty results), exit gracefully.
    - For each pulse: extract name, tags, indicators
    - Assign priority: HIGH / MEDIUM / LOW (case-insensitive tag logic)
    - Compute indicator count for each pulse
    - Write a report to 'otx_intelligence_report.txt'
    """
    pass