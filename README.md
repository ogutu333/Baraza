# OTX Threat Intelligence

A Python-based threat intelligence tool that interacts with AlienVault's Open Threat Exchange (OTX) API to collect, analyze, and prioritize threat intelligence data.

## Overview

This script provides automated threat intelligence collection from OTX, helping security analysts:
- Collect subscribed threat pulse data (IOCs, TTPs)
- Parse and validate raw API responses
- Contextualize and prioritize threats (HIGH/MEDIUM/LOW)
- Export structured intelligence reports

## Author

**Deborah Ogutu**  
Date: 2026-05-18

## Features

- **Automated Threat Collection**: Fetches subscribed pulses from OTX API
- **Intelligent Prioritization**: Automatically classifies threats as HIGH or LOW based on keywords
- **Structured Reporting**: Generates human-readable text reports with threat details
- **Error Handling**: Gracefully handles HTTP errors, empty data, and missing fields
- **Sample Indicators**: Displays first 5 indicators per pulse for quick assessment

## Priority Classification

| Priority | Keywords |
|----------|----------|
| **HIGH** | ransomware, phishing, malware, trojan, APT, exploit, zeroday, CVE, botnet |
| **LOW** | Everything else |

## Prerequisites

- Python 3.6 or higher
- Internet connection for OTX API access
- (Optional) OTX API key for higher rate limits

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/ogutu333/Baraza.git
cd Baraza
```

2. **Install required dependencies:**
```bash
pip install requests
```

3. **Set up virtual environment:**
```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install requests
```

# Usage
## Basic Usage
```bash
python otx.py
```

## With Custom API Key
Edit the fetch_threat_intelligence() function and replace the API key:
```python
headers = {
    'X-OTX-API-Key': 'YOUR_API_KEY_HERE'
}
```

## Output
The script generates otx_intelligence_report.txt with:
```text
================================================================================
OTX THREAT INTELLIGENCE REPORT
Generated: 2026-05-18 17:18:38
================================================================================

SUMMARY:
  Total Pulses: 5
  HIGH Priority Threats: 3
  LOW Priority Threats: 2

================================================================================

Pulse #1: Tracking Mirai Variant Nexcorium: A Vulnerability-Driven IoT Botnet Campaign
  Priority: 🔴 HIGH
  Created: 2026-04-17T18:56:13.678000
  Indicator Count: 20
  Description: Nexcorium is a multi-architecture Mirai variant exploiting CVE-2024-3721 in TBK DVR devices to build a botnet for distributed denial-of-service attack...
  Tags: cve-2024-3721, mirai variant, mirai, persistence mechanisms, iot botnet, multi-architecture, credential brute-force, tbk dvr exploitation, nexcorium, ddos attacks and 1 more
  Sample Indicators (5 of 20):
    1. [CVE] CVE-2017-17215
    2. [CVE] CVE-2024-3721
    3. [FileHash-MD5] aaed4dca8bd6bb42fc4efb358a02a554
    4. [FileHash-SHA1] ebdae1b6a28589ecc8d84557f0e83963396291cf
    5. [FileHash-SHA256] 89dae116c77b0035277d39dfe01043624427c119ddee8883a3ba54a42a6ae400

--------------------------------------------------------------------------------

Pulse #2: Live off the Land? How About Bringing Your Own Island? An Overview of UNC1945
  Priority: 🔴 HIGH
  Created: 2026-04-17T18:32:58.889000
  Indicator Count: 16
  Description: UNC1945 compromised managed service providers to target organizations within financial and professional consulting industries through third-party netw...
  Tags: evilsun, financial sector, lemonstick, steelcorgi, rollcoast, pam backdoor, oracle solaris, cve-2019-0708, managed service providers, oksolo and 10 more
  Sample Indicators (5 of 16):
    1. [FileHash-MD5] 6983f7001de10f4d19fc2d794c3eb534
    2. [CVE] CVE-2019-0708
    3. [FileHash-MD5] d505533ae75f89f98554765aaf2a330a
    4. [FileHash-MD5] 2eff2273d423a7ae6c68e3ddd96604bc
    5. [FileHash-MD5] 0845835e18a3ed4057498250d30a11b1

--------------------------------------------------------------------------------

Pulse #3: Untangling a Linux Incident With an OpenAI Twist
  Priority: 🟢 LOW
  Created: 2026-04-17T14:19:42.479000
  Indicator Count: 1
  Description: A technology sector organization experienced a multi-actor compromise on a Linux endpoint where cryptominers were deployed and credential harvesting o...
  Tags: codex ai, multi-actor, living-off-the-land, linux compromise, edr evasion, credential theft, monero mining, cryptominer
  Sample Indicators (1 of 1):
    1. [CVE] CVE-2025-47812

--------------------------------------------------------------------------------

Pulse #4: Dissecting macOS intrusion from lure to compromise
  Priority: 🟢 LOW
  Created: 2026-04-17T08:37:43.088000
  Indicator Count: 16
  Description: Microsoft Threat Intelligence uncovered a macOS-focused cyber campaign by North Korean threat actor Sapphire Sleet utilizing social engineering to com...
  Tags: social engineering, north korea, systemupdate.app, tcc bypass, com.google.chromes.updaters, applescript, services, softwareupdate.app, cryptocurrency theft, com.apple.cli and 4 more
  Sample Indicators (5 of 16):
    1. [domain] uw04webzoom.us
    2. [domain] ur01webzoom.us
    3. [domain] uv01webzoom.us
    4. [FileHash-SHA256] 05e1761b535537287e7b72d103a29c4453742725600f59a34a4831eafc0b8e53
    5. [FileHash-SHA256] 2075fd1a1362d188290910a8c55cf30c11ed5955c04af410c481410f538da419

--------------------------------------------------------------------------------

Pulse #5: CVE-2026-39987 update: How attackers weaponized marimo to deploy a blockchain botnet via HuggingFace
  Priority: 🔴 HIGH
  Created: 2026-04-16T08:36:45.830000
  Indicator Count: 10
  Description: Three days after disclosure of a critical pre-authorization remote code execution vulnerability in the marimo Python notebook platform, multiple threa...
  Tags: huggingface, cve-2026-39987, nkn blockchain, marimo
  Sample Indicators (5 of 10):
    1. [CVE] CVE-2017-5638
    2. [CVE] CVE-2026-39987
    3. [FileHash-MD5] 1d36de06a6240919189cb46e0bcccc3c
    4. [FileHash-MD5] bdcb5867f73beae89c3fce46ad5185be
    5. [FileHash-SHA1] 049c35fa746a8b86c100bf6b348ef6163b215898

--------------------------------------------------------------------------------
```

## Algorithm Workflow
```text
1. FETCH Threat Intelligence
   └── GET /api/v1/pulses/subscribed with API key
   └── Return parsed JSON or None

2. PARSE Intelligence Data
   └── Validate data structure
   └── Extract: name, tags, indicators, counts
   └── Assign priority based on keywords
   └── Generate report

3. DISPLAY Results
   └── Console summary
   └── Write detailed report to .txt file
```

## Console Output
```bash
$ python otx.py
Fetching threat intelligence from OTX...
Successfully retrieved data. Processing...
Report successfully written to 'otx_intelligence_report.txt'

================================================================================
OTX THREAT INTELLIGENCE REPORT
Generated: 2026-05-18 17:18:38
================================================================================

SUMMARY:
  Total Pulses: 5
  HIGH Priority Threats: 3
  LOW Priority Threats: 2
...
```

# Function Documentation

| Function | Parameters | Description | Returns |
|----------|------------|-------------|---------|
| `fetch_threat_intelligence()` | None | Fetches subscribed pulses from OTX API using configured headers | `dict` (JSON) or `None` |
| `parse_threat_intelligence(data)` | `data` (JSON response) | Parses threat data, assigns priorities, and extracts IOCs | `list` of processed pulse dictionaries |
| `write_report(processed_pulses)` | `processed_pulses` (list) | Generates formatted text report and saves to file | `None` |

## Error Handling
The script handles:
- **HTTP Errors:** Non-200 status codes
- **Network Issues:** Connection timeouts
- **Empty Data:** No pulses or invalid JSON
- **Missing Fields:** Graceful fallbacks to defaults
- **File I/O Errors:** Permission or disk space issues

## Security Notes
- **API Key:** The included key is for demonstration. Request your own from OTX > https://otx.alienvault.com
- **Rate Limits:** Unauthenticated requests have lower limits. Use an API key for production.
- **Data Privacy:** All processing is local. No data is sent except to OTX API.

# Troubleshooting
## Common Issues
**Issue:** ImportError: No module named requests
```bash
pip install requests
```

**Issue:** Error: Received status code 403
- Your API key is invalid or expired
- Generate a new key from OTX settings

**Issue:** No pulses found in the results
- Subscribe to pulses on OTX dashboard first
- Check if your account has subscribed threats

**Issue:** Failed to retrieve threat intelligence data
- Check your internet connection
- Verify OTX API is accessible

# License
This project is for educational purposes as part of Applied Cyber Threat Intelligence coursework at Moringa.
