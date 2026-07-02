import boto3
import requests
import time

# Function to simulate listing API Gateways
def list_apis():
    """
    Simulates fetching API Gateways from AWS.
    Instead of calling AWS, we return mock data.
    """
    return [
        {"id": "abc123", "name": "PublicAPI"},
        {"id": "xyz789", "name": "SecureAPI"}
    ]

# Function to check API security configurations
def check_api_security(api_id):
    """
    Scope of this script:
    - Scan AWS API Gateway configurations.
    - Check for:
        * Missing authentication mechanisms.
        * Weak authentication methods.
        * Insecure HTTP usage (HTTPS not enforced).
        * Overly permissive CORS settings.
    - This script simulates API security scanning using mock data.
    """

    # Simulated API configurations
    mock_api_configurations = {
        "abc123": {
            "auth_type": "NONE",
            "use_https": False,
            "cors": "*"
        },
        "xyz789": {
            "auth_type": "COGNITO_AUTH",
            "use_https": True,
            "cors": "restricted"
        }
    }

    api_config = mock_api_configurations.get(api_id, {})

    print(f"\nChecking API {api_id} for security issues...\n")

    # Store findings in a dictionary
    findings = {
        "Missing Authentication": False,
        "Weak Authentication": False,
        "HTTPS Enforced": True,
        "Permissive CORS": False,
        "Unauthorized Access": False
    }

    # Check for missing authentication
    if api_config.get("auth_type") == "NONE":
        print("WARNING: API has NO authentication! This API is open to the public.\n")
        findings["Missing Authentication"] = True

    # Check for weak authentication
    if api_config.get("auth_type") == "BASIC_AUTH":
        print("WARNING: API uses Basic Authentication. Consider OAuth2.\n")
        findings["Weak Authentication"] = True

    # Check HTTPS enforcement
    if not api_config.get("use_https"):
        print("WARNING: API does not enforce HTTPS! Data might be exposed in transit.\n")
        findings["HTTPS Enforced"] = False

    # Check CORS settings
    if api_config.get("cors") == "*":
        print("WARNING: API has overly permissive CORS settings. May allow cross-origin attacks.\n")
        findings["Permissive CORS"] = True

    # Simulate sending an unauthorized request
    url = f"https://{api_id}.execute-api.amazonaws.com"

    print(f"Sending test request to {url}...\n")

    try:
        response = requests.get(url)

        if response.status_code == 200:
            print("WARNING: API is accessible without authentication!\n")
            findings["Unauthorized Access"] = True
        else:
            print("API requires authentication.\n")
    except:
        print("Unable to connect to the API (simulated scenario).\n")

    # Print security findings
    print("Security Findings:")
    for key, value in findings.items():
        print(f"{key}: {value}")
    print()


# Main function
if __name__ == "__main__":
    while True:
        print("Running API Security Scan...\n")

        apis = list_apis()

        if not apis:
            print("No APIs found.")
        else:
            for api in apis:
                print(f"\nScanning API: {api['name']} (ID: {api['id']})")
                check_api_security(api["id"])

        print("\nNext scan in 5 minutes...\n")
        time.sleep(300)
