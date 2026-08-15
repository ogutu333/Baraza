# Reconnaissance Part 2

## Overview

This lab focused on using **Google dorking** as part of the reconnaissance process. The goal was to create a Python script that automates Google searches using predefined search operators and stores the results for later analysis.

I started with a partially completed Python script and developed it into `dork_final.py`. The script can generate Google dorking queries, send search requests, parse the returned HTML, and save the results to a text file.

The lab also introduced basic error handling, custom user queries and the ability to skip queries that had already been completed.

> **Note:** This lab was completed for educational and security research purposes. Google dorking should only be used to investigate systems, domains and information that you are authorised to assess.

## Objectives

The script was designed to:

- Automate Google searches using predefined dorking queries.
- Search for potentially exposed login pages.
- Search for publicly accessible documents.
- Search for potentially exposed directory listings or databases.
- Allow the user to enter an additional custom query.
- Parse URLs from Google's search response.
- Save search results to a text file.
- Handle request errors without crashing.
- Resume searches by skipping previously completed queries.

## Technologies and Tools Used

- **Python 3**
- **VS Code**
- `requests`
- `BeautifulSoup`
- `time`
- `os`
- **Google Search**
- Google dorking/search operators

## Project Structure

```text
reconnaissance-part-2/
│
├── dork_final.py
├── dorking_results.txt
└── README.md
```

## Lab Tasks

### Task 1 — Determine the Scope and Functionality

I started with the provided `dork_starter.py` script and reviewed what the program needed to accomplish.

The script was designed to automate searches using predefined Google dorking queries.

The main searches were:

- `inurl:login` — search for pages containing `login` in the URL.
- `filetype:pdf OR filetype:doc` — search for publicly accessible PDF or DOC files.
- `intitle:index.of mysql` — search for pages that may contain directory listings related to MySQL.

I then renamed the starter script to:

```text
dork_final.py
````

### Task 2 — Add Functions to the Script

I added separate functions for generating queries, sending requests and processing search results.

The `generate_dork_queries()` function creates the predefined queries:

```python
def generate_dork_queries():
    """Generate Google dorking queries for security research."""

    queries = [
        "inurl:login",
        "filetype:pdf OR filetype:doc",
        "intitle:index.of mysql"
    ]

    return queries
```

This made it easier to manage and add additional queries later.

I also created the `send_search_request()` function to send the queries to Google.

The `parse_search_results()` function uses BeautifulSoup to process the returned HTML and extract URLs.

### Task 3 — Integrate Google Search Requests

I created the `perform_dorking()` function to connect the different parts of the script.

The process works by:

1. Loading the predefined Google dorking queries.
2. Asking the user if they want to add a custom query.
3. Checking whether previous searches already exist in the results file.
4. Skipping queries that have already been completed.
5. Sending the remaining queries to Google.
6. Parsing the returned search results.
7. Waiting two seconds between requests.

The two-second delay was included to avoid sending requests too quickly.

```python
time.sleep(2)
```

### Task 4 — Process and Store Search Results

The `save_results()` function saves the collected URLs into:

```text
dorking_results.txt
```

The results are organised according to the query that produced them.

For example:

```text
Results for: inurl:login
```

URL results appear here.

The file is opened in append mode:

```python
with open("dorking_results.txt", "a") as file:
```

This allows new results to be added without deleting previous results.

### Task 5 — Test and Debug the Script

I integrated the different functions into the `main()` function.

The script can be started from the terminal using:

```bash
python dork_final.py
```

When it starts, it displays:

```text
Welcome to the Automated Google Dorking Script!
```

It then asks:

```text
Enter an additional Google dork query (or press Enter to skip):
```

I tested the script using the predefined queries and also tested a custom query such as:

```text
tomatoes
```

The results were saved to `dorking_results.txt`.

### Task 6 — Enhance and Secure the Script

I added error handling to the `send_search_request()` function using `try` and `except`.

```python
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
```

This means that if the request fails, the script displays an error instead of crashing.

I also added support for custom queries so that the user can perform additional searches.

The script can also resume previous searches by checking `dorking_results.txt` and identifying queries that have already been completed.

### Task 7 — Documentation

I added comments and docstrings throughout the script to explain what the different functions do.

The script also contains a README-style description explaining:

* The purpose of the script.
* Its main features.
* Required Python libraries.
* How to install dependencies.
* How to run the script.

The required libraries can be installed using:

```bash
pip install requests beautifulsoup4
```

## Example Results

The script generated a `dorking_results.txt` file containing results for the different queries.

### Login Page Search

The first query was:

```text
Results for: inurl:login
```

The results included:

```text
/httpservice/retry/enablejs?sei=...
https://support.google.com/websearch
```

### Public Document Search

The second query was:

```text
Results for: filetype:pdf OR filetype:doc
```

The results included Google's search-related URLs.

### Open Directory Search

The third query was:

```text
Results for: intitle:index.of mysql
```

The script successfully processed the query and stored the returned URLs.

### Custom Search

I also tested the custom query functionality using:

```text
tomatoes
```

The results were saved under:

```text
Results for: tomatoes
```

The results demonstrate that the script was able to process both predefined and user-provided queries.

> **Note:** The returned URLs were not necessarily vulnerable systems. Search results can include unrelated pages, redirects or Google's own search-support URLs. Further manual validation would be required before treating a result as a genuine security finding.

## 🔍 Key Cybersecurity Concepts Learned

### Google Dorking

Google dorking uses advanced search operators to locate specific types of publicly indexed information.

Examples include:

* `inurl:`
* `filetype:`
* `intitle:`

These operators can help security professionals identify information that an organisation may not realise is publicly searchable.

### Reconnaissance

Google dorking is useful during the reconnaissance phase of a security assessment because it can reveal information about an organisation without directly scanning its systems.

### Attack Surface

Publicly indexed login pages, documents and directory listings can provide information about an organisation's external attack surface.

Understanding what is publicly exposed allows defenders to identify and reduce unnecessary exposure.

### Web Scraping

The script uses **BeautifulSoup** to process HTML returned from the search request and extract links.

This gave me practical experience with basic HTML parsing and extracting information from web responses.

### HTTP Requests

The `requests` library was used to communicate with Google's search endpoint.

I learned how to:

* Build URLs.
* Send GET requests.
* Add HTTP headers.
* Check HTTP status codes.
* Process response data.

### Error Handling

The script uses `try` and `except` blocks to handle request failures.

This is important because external services can reject requests, become unavailable or return unexpected responses.

### Automation

Instead of manually running each Google search, the Python script performs multiple searches automatically.

This showed me how scripting can make repetitive reconnaissance tasks faster and more consistent.

### Data Storage

The results are stored in a text file so they can be reviewed later.

This is useful during reconnaissance because results can be collected first and analysed separately.

## What I Learned

This lab helped me understand how search engines can be used as an OSINT and reconnaissance source.

I learned that information does not always need to be obtained by directly scanning a target. Search engines can already index documents, login pages and other publicly accessible information.

I also got more practice with Python functions, HTTP requests, HTML parsing, file handling and error handling.

Another useful part of the lab was adding the resume functionality. Instead of repeating searches that had already been completed, the script checks the existing results file and skips those queries.

## Limitations

This is a basic educational Google dorking script and has several limitations:

* Google may block or restrict automated requests.
* Search results can change over time.
* The script does not verify whether a discovered resource is actually exposed or vulnerable.
* The HTML structure of Google search results can change.
* The parser may collect unrelated URLs.
* The script does not perform deep analysis of discovered documents.
* It does not automatically identify whether credentials or sensitive information are exposed.
* Search results may include Google's own support or redirect URLs.
* It does not provide comprehensive search engine coverage.

The script should therefore be treated as an introductory reconnaissance automation project rather than a complete OSINT framework.

## Possible Improvements

If I continued developing this project, I could:

* Improve the Google result parser.
* Remove duplicate URLs.
* Filter out Google's own URLs.
* Add domain-specific searches.
* Add more Google dorking operators.
* Export results to JSON or CSV.
* Add timestamps to search results.
* Add better logging.
* Add command-line arguments.
* Add configurable search delays.
* Add result validation.
* Add support for other search engines where permitted.
* Create a simple interface for managing queries and results.

## Security+ Connection

This lab relates to **CompTIA Security+** concepts including:

* Reconnaissance
* Open-Source Intelligence (OSINT)
* Attack surface
* Information exposure
* Social engineering
* Threat identification
* Security assessment
* Vulnerability identification

Google dorking is particularly relevant to reconnaissance because attackers can use publicly indexed information to learn about an organisation before attempting further attacks.

Defenders can use similar techniques to identify information that their organisation may be unintentionally exposing online.

## Security Considerations

Google dorking should only be performed for authorised security research.

The purpose of this lab was to understand how publicly available information can be discovered and how defenders can identify potential exposure.

The script does not attempt to exploit any discovered systems. Finding a login page, document or directory listing does not automatically mean that the system is vulnerable.

Any findings should be manually verified within the scope of an authorised security assessment.

## Skills Demonstrated

This lab demonstrates practical experience with:

* Python scripting
* Google dorking
* OSINT
* Reconnaissance
* Search operators
* HTTP requests
* Web scraping
* BeautifulSoup
* HTML parsing
* File handling
* Error handling
* Automation
* Security documentation

## Conclusion

Overall, this lab gave me practical experience using **Python to automate reconnaissance and Google dorking**.

I created a script that generates predefined searches, allows additional user queries, sends requests to Google, parses returned URLs and saves the results for later analysis.

The lab also helped me understand how much information can potentially be discovered through search engines and why organisations should regularly review what information about their systems and employees is publicly accessible.

It was a useful continuation of the first reconnaissance lab because I moved from collecting WHOIS and Shodan information to using search engines as another source of OSINT.