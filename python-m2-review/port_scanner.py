def scan_ports(start_port, end_port):
    for port in range(start_port, end_port + 1):
        print("Scanning port", port, "...")

# Call the function
scan_ports(20, 25)