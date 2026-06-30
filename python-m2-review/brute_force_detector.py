logs = [
    "192.168.1.50 - successful login",
    "10.0.0.15 - failed login",
    "192.168.1.50 - successful login",
    "10.0.0.15 - failed login",
    "172.16.0.4 - successful login",
    "10.0.0.15 - failed login",
    "10.0.0.15 - failed login"
]

failed_logins = {}

for log in logs:
    if "failed login" in log:
        ip = log.split(" - ")[0]

        if ip in failed_logins:
            failed_logins[ip] += 1
        else:
            failed_logins[ip] = 1

        if failed_logins[ip] >= 3:
            print("ALERT: Brute-force detected from IP", ip)
            break