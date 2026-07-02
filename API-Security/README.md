# API Security Scanner (Simulated)

## Overview

This project is a simulated API security scanner written in Python. It demonstrates how an AWS API Gateway security assessment could be performed using mock API data instead of connecting to real AWS resources.

The script scans for common API security misconfigurations and displays a report of any findings.

## Features

- Simulates AWS API Gateway data
- Checks for missing authentication
- Checks for weak authentication methods
- Verifies HTTPS enforcement
- Detects overly permissive CORS settings
- Simulates unauthorized API requests
- Displays a security findings report
- Supports scheduled scanning every five minutes

## Requirements

- Python 3.x
- boto3
- requests

Install the required libraries:

```bash
pip install boto3 requests
```

## Project Files

- `API_final.py` – Main Python script that performs the simulated API security scan.
- `README.md` – Documentation for the project.

## How It Works

The script uses mock API Gateway data to simulate an AWS environment. For each API, it performs the following checks:

1. Checks whether authentication is enabled.
2. Looks for weak authentication methods.
3. Verifies that HTTPS is enforced.
4. Checks for overly permissive CORS settings.
5. Simulates an unauthorized request to test API security.

After each scan, the script displays a security report showing any vulnerabilities that were found.

## Running the Script

Run the script with:

```bash
python API_final.py
```

The scanner will continue running and automatically perform a new scan every five minutes until it is stopped.

## Notes

- This project is intended for educational purposes.
- No AWS credentials are required because all API Gateway data is simulated.
- The script demonstrates the basic workflow of an API security scanner without interacting with real AWS services.

## License

This project was provided by Moringa School.