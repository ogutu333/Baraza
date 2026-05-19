"""
=============================================================================================
FILE     : otx.py
AUTHOR   : Deborah Ogutu
DATE     : 2026-05-18
DESCRIPTION : Applied Cyber Threat Intelligence (CTI) script that interacts
              with AlienVault's Open Threat Exchange (OTX) API to:
                - Collect subscribed threat pulse data (IOCs, TTPs)
                - Parse and validate the raw API response
                - Contextualize and prioritize threats (HIGH/MEDIUM/LOW)
                - Export a structured intelligence report to a .txt file

ALGORITHM   :
    1. PROBLEM   : Collect, parse, prioritize, and report OTX threat intelligence
    2. PSEUDOCODE:
         fetch_threat_intelligence()
             → GET OTX subscribed pulses endpoint with API key header
             → Return parsed JSON on success, None on failure

         parse_threat_intelligence(data)
             → Validate data; exit gracefully if None/empty
             → For each pulse: extract name, tags, indicators, indicator count
             → Assign priority: HIGH (ransomware/phishing/APT/malware)
                                MEDIUM (trojan/botnet/backdoor/exploit/spam)
                                LOW (everything else)
             → Print summary to console
             → Write full report to otx_intelligence_report.txt

         __main__
             → Call fetch → pass result to parse

    3. CODE      : (this file)
    4. EXECUTE   : python otx.py
    5. DEBUG     : Handles HTTP errors, empty data, and missing fields gracefully
    6. DOCUMENT  : Inline comments throughout; docstrings on every function

REFERENCES  :
    - AlienVault OTX API docs: https://otx.alienvault.com/api
    - URLHaus CTI example from course PDF (Applied Cyber Threat Intelligence)
=============================================================================================
"""

import requests
import json
from datetime import datetime

def fetch_threat_intelligence():
    url = 'https://otx.alienvault.com/api/v1/pulses/subscribed'
    headers = {
        'X-OTX-API-KEY': '8bac38a96c44c3fb4d847fc517774706f978c5728caa6675bc933ac2e33a72c6'  # Optional: only needed for live runs
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
    Parse and analyze threat intelligence data from OTX.
    
    Args:
        data: JSON response from OTX API
    
    Returns:
        List of processed pulses with priority and indicator counts
    """
    # Validate the retrieved data
    if not data:
        print("No data received. Exiting gracefully.")
        return None
    
    if 'results' not in data:
        print("Invalid data format: 'results' key not found.")
        return None
    
    if not data['results']:
        print("No pulses found in the results.")
        return None
    
    # High priority keywords (case-insensitive)
    high_priority_keywords = ['ransomware', 'phishing', 'malware', 'trojan', 
                              'apt', 'exploit', 'zeroday', 'cve', 'botnet']
    
    processed_pulses = []
    
    # Process each pulse
    for pulse in data['results']:
        # Extract basic information
        name = pulse.get('name', 'Unnamed Pulse')
        tags = pulse.get('tags', [])
        indicators = pulse.get('indicators', [])
        indicator_count = len(indicators)
        
        # Determine priority based on tags (case-insensitive)
        priority = 'LOW'
        for tag in tags:
            if any(keyword in tag.lower() for keyword in high_priority_keywords):
                priority = 'HIGH'
                break
        
        # Store processed pulse information
        processed_pulse = {
            'name': name,
            'tags': tags,
            'indicators': indicators[:5] if indicators else [],  # First 5 indicators for display
            'indicator_count': indicator_count,
            'priority': priority,
            'created': pulse.get('created', 'Unknown date'),
            'description': pulse.get('description', 'No description provided')
        }
        processed_pulses.append(processed_pulse)
    
    # Display in human-readable format and write to file
    write_report(processed_pulses)
    
    return processed_pulses

def write_report(processed_pulses):
    """
    Write the prioritized threat intelligence data to a text file and display it.
    
    Args:
        processed_pulses: List of processed pulse dictionaries
    """
    if not processed_pulses:
        print("No processed pulses to report.")
        return
    
    # Generate report content
    report_lines = []
    report_lines.append("=" * 80)
    report_lines.append("OTX THREAT INTELLIGENCE REPORT")
    report_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append("=" * 80)
    report_lines.append("")
    
    # Count priorities
    high_count = sum(1 for p in processed_pulses if p['priority'] == 'HIGH')
    low_count = len(processed_pulses) - high_count
    
    report_lines.append(f"SUMMARY:")
    report_lines.append(f"  Total Pulses: {len(processed_pulses)}")
    report_lines.append(f"  HIGH Priority Threats: {high_count}")
    report_lines.append(f"  LOW Priority Threats: {low_count}")
    report_lines.append("")
    report_lines.append("=" * 80)
    report_lines.append("")
    
    # Process each pulse for detailed display
    for idx, pulse in enumerate(processed_pulses, 1):
        # Priority indicator
        priority_symbol = "🔴 HIGH" if pulse['priority'] == 'HIGH' else "🟢 LOW"
        
        report_lines.append(f"Pulse #{idx}: {pulse['name']}")
        report_lines.append(f"  Priority: {priority_symbol}")
        report_lines.append(f"  Created: {pulse['created']}")
        report_lines.append(f"  Indicator Count: {pulse['indicator_count']}")
        report_lines.append(f"  Description: {pulse['description'][:150]}..." if len(pulse['description']) > 150 else f"  Description: {pulse['description']}")
        
        # Tags
        if pulse['tags']:
            tag_str = ", ".join(pulse['tags'][:10])  # Show first 10 tags
            if len(pulse['tags']) > 10:
                tag_str += f" and {len(pulse['tags']) - 10} more"
            report_lines.append(f"  Tags: {tag_str}")
        else:
            report_lines.append(f"  Tags: None")
        
        # Indicators (sample)
        if pulse['indicators']:
            report_lines.append(f"  Sample Indicators ({min(5, len(pulse['indicators']))} of {pulse['indicator_count']}):")
            for i, indicator in enumerate(pulse['indicators'][:5], 1):
                indicator_type = indicator.get('type', 'unknown')
                indicator_value = indicator.get('indicator', 'unknown')
                report_lines.append(f"    {i}. [{indicator_type}] {indicator_value}")
        else:
            report_lines.append(f"  Indicators: None")
        
        report_lines.append("")
        report_lines.append("-" * 80)
        report_lines.append("")
    
    # Write to file
    try:
        with open('otx_intelligence_report.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(report_lines))
        print("Report successfully written to 'otx_intelligence_report.txt'")
    except Exception as e:
        print(f"Error writing report to file: {e}")
    
    # Also display to console
    print('\n'.join(report_lines))

def main():
    """
    Main function to fetch and process threat intelligence.
    """
    print("Fetching threat intelligence from OTX...")
    data = fetch_threat_intelligence()
    
    if data:
        print("Successfully retrieved data. Processing...")
        parse_threat_intelligence(data)
    else:
        print("Failed to retrieve threat intelligence data.")

if __name__ == '__main__':
    main()