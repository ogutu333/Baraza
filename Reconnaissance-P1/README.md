# Reconnaissance Part 1 

## Overview

This lab focused on using **Open-Source Intelligence (OSINT)** techniques to collect publicly available information about a domain.

Created a Python script that uses **WHOIS** and the **Shodan API** to gather information about a target domain. The results are displayed in the terminal and saved into a JSON report.

The main purpose of the lab was to understand how much information about an organisation can be collected without directly interacting with its internal systems.

> **Note:** This lab was completed for educational purposes using publicly available information. OSINT activities should only be performed on domains and organisations where you have permission to conduct the assessment.

## Objectives

The script was designed to:

- Collect WHOIS information about a domain.
- Resolve the domain to an IP address using Shodan.
- Retrieve Shodan information about the resolved IP.
- Identify publicly exposed services and ports where Shodan provides the information.
- Display the collected information in the terminal.
- Save the results into a JSON file.
- Use a User-Agent header when making API requests.
- Handle errors when information cannot be retrieved.

## Technologies and Tools Used

- **Python 3**
- **VS Code**
- `requests` library
- `python-whois` library
- **Shodan API**
- **WHOIS**
- **JSON**

## Project Structure

```text
reconnaissance-part-1/
│
├── OSINT_final.py
├── microsoft.com_osint.json
├── apple.com_osint_report.json
└── README.md
```

## Lab Tasks

### Task 1 — Determine the Scope and Functionality

The script needed to collect:

1. WHOIS information
2. Domain-related information
3. Shodan information
4. Results that could be saved for later analysis

Rename the starter script to:

```text
OSINT_final.py
```

### Task 2 — Add WHOIS Functionality

Added the **get_whois_info()** function to retrieve registration information about the target domain.

The function uses the **whois library** and returns the available WHOIS information.

The information can include details such as:
- Domain name
- Registrar
- Creation date
- Expiration date
- Name servers
- Domain status
- Organisation information
- Contact information where it is publicly available

The function also includes error handling so the script can return an error message instead of stopping completely if the WHOIS lookup fails.

### Task 3 — Integrate Shodan

Added a `get_shodan_info()` function to query the Shodan API.

The process works by:

- Taking the domain entered by the user.
- Sending a request to Shodan's DNS resolution endpoint.
- Obtaining the IP address associated with the domain.
- Using the IP address to query Shodan for host information.
- Returning the results as formatted JSON.

A User-Agent header was also added to the requests:

```python
headers = {
    "User-Agent": "Mozilla/5.0"
}
```

The Shodan API key is stored in a variable:

```python
SHODAN_API_KEY = "your_shodan_api_key_here"
```

The API key should not be hardcoded into a public GitHub repository. In a real project, I would store it in an environment variable or another secure secret-management method.

### Task 4 — Store and Format the Results

The WHOIS and Shodan results are stored in a Python dictionary:

```python
osint_results = {
    "WHOIS": whois_data,
    "Shodan": shodan_data
}
```

The dictionary is then saved as a JSON file using:

```python
json.dump(osint_results, outfile, indent=4)
```

This makes the collected information easier to read, store and analyse later.

### Task 5 — Test the Script

Tested the script using publicly known domains such as:

* `microsoft.com`
* `apple.com`

The script prompts for a domain:

```text
Enter the domain name to investigate:
```

After entering the domain, the script performs the WHOIS and Shodan lookups and saves the results to a JSON report.

For example:

```bash
python OSINT_final.py
```

The output includes sections for:

```text
[WHOIS Information]:

[Shodan Information]:
```

### Task 6 — Add a User-Agent Header

Modified the Shodan API requests to include a User-Agent header.

This was added to the `requests.get()` calls:

```python
response = requests.get(url, headers=headers)
```

and:

```python
shodan_response = requests.get(shodan_url, headers=headers)
```

This demonstrates how HTTP requests can include headers when communicating with external services.

### Task 7 — Documentation

Added comments and docstrings to explain the purpose of the script and its functions.

For example:

```python
def get_whois_info(domain):
    """Fetches WHOIS information for a given domain."""
```

The script also includes a description explaining its purpose and how to run it.

#### Example Results

##### Microsoft

The WHOIS lookup returned information including:

* Domain name: `MICROSOFT.COM`
* Registrar information
* Creation date
* Expiration date
* Azure DNS name servers
* Domain status
* Organisation information

The Shodan lookup returned:

```text
No IP found for this domain.
```

This shows that an unsuccessful Shodan lookup does not necessarily mean that the domain has no publicly available information.

##### Apple

The WHOIS lookup returned information including:

* Domain name: `APPLE.COM`
* Registrar: Nom-iq Ltd. dba COM LAUDE
* Creation date
* Expiration date
* Apple name servers
* Domain status
* Some organisation information

The available WHOIS data also demonstrated how some registrant information is redacted for privacy.

The Shodan result was:

```text
No IP found for this domain.
```

## Key Cybersecurity Concepts Learned

### Open-Source Intelligence (OSINT)

OSINT involves collecting and analysing information that is publicly available. This can include domain registration records, DNS information, public infrastructure details and other information exposed online.

### Reconnaissance

Reconnaissance is an important part of security assessments because it helps identify information about a target before further security testing takes place.

### WHOIS Enumeration

WHOIS can reveal useful information about domain registration, including registrar details, registration dates, name servers and sometimes organisation or contact information.

### Shodan

Shodan is useful for identifying information about internet-facing systems and services. It can provide information about exposed ports, services, banners and other host information when available.

### API Integration

This lab gave me practical experience using an external API from Python. I learned how to construct API requests, process JSON responses and handle errors.

### JSON Data Storage

Saving the results as JSON makes the information easier to organise and use in other tools or scripts.

### Error Handling

The functions use `try` and `except` blocks to handle errors during WHOIS and Shodan requests. This prevents one failed lookup from immediately crashing the program.

## What I Learned

This lab helped me understand how much information can potentially be gathered about an organisation using publicly available sources.

I also got more practice working with Python libraries, APIs, JSON data and error handling.

One of the main things I learned is that reconnaissance does not always involve directly scanning a target. Public information such as domain registration records and exposed infrastructure can already provide useful information about an organisation's external footprint.

## Limitations

This script is a basic OSINT tool and has several limitations:

* The Shodan API requires an API key.
* Shodan may not return information for every domain.
* WHOIS information can be redacted or limited.
* The script only performs a small number of OSINT checks.
* It does not perform comprehensive DNS enumeration.
* It does not collect subdomains.
* It does not search social media or public documents.
* API availability and results can change over time.

The script should therefore be treated as an introductory OSINT project rather than a complete reconnaissance framework.

## Possible Improvements

If I continued developing this project, I could:

* Add DNS enumeration.
* Add subdomain discovery.
* Add reverse DNS lookups.
* Add certificate transparency searches.
* Add email/domain enumeration.
* Add more OSINT sources.
* Improve the JSON report structure.
* Add timestamps to each report.
* Add command-line arguments instead of relying only on `input()`.
* Store the Shodan API key in an environment variable.
* Add logging and more detailed error handling.
* Create a simple web interface for viewing reports.

## Security+ Connection

This lab relates to **CompTIA Security+** concepts including:

* Reconnaissance
* Open-Source Intelligence (OSINT)
* Attack surface
* Network services
* DNS
* Publicly exposed information
* Security assessment
* Threat identification

Understanding reconnaissance is important because attackers can use publicly available information to identify potential targets, while defenders can use the same techniques to understand and reduce their organisation's external exposure.

## Security Considerations

The Shodan API key should be treated as a secret.

I would **not commit an actual API key to GitHub**. Instead, I would use an environment variable such as:

```bash
export SHODAN_API_KEY="your_api_key"
```

and retrieve it from Python using:

```python
import os

SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")
```

This reduces the risk of accidentally exposing credentials in a public repository.

## Skills Demonstrated

This lab demonstrates practical experience with:

* Python scripting
* OSINT
* Reconnaissance
* WHOIS enumeration
* API integration
* Shodan
* HTTP requests
* JSON processing
* Error handling
* Data storage
* Security documentation

## Conclusion

Overall, this lab gave me practical experience with **OSINT and reconnaissance using Python**. I created a script that can collect WHOIS information and query Shodan for publicly available host information, then save the results into a JSON report.

The lab also showed me how attackers can use publicly available information during the reconnaissance stage and why organisations need to understand what information about their infrastructure is exposed online.

It was a useful introduction to automating OSINT tasks instead of manually collecting each piece of information.