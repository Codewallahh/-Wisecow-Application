#!/usr/bin/env python3
import re
from collections import defaultdict

log_file = "/var/log/nginx/access.log"
report_file = "log_report.txt"

def analyze_logs():
    ip_requests = defaultdict(int)
    pages_requested = defaultdict(int)
    error_404 = 0

    with open(log_file, 'r') as file:
        logs = file.readlines()

    for log in logs:
        ip_match = re.search(r'(\d+\.\d+\.\d+\.\d+)', log)
        page_match = re.search(r'GET\s(\/\S+)', log)
        error_match = re.search(r' 404 ', log)

        if ip_match:
            ip_requests[ip_match.group(1)] += 1
        if page_match:
            pages_requested[page_match.group(1)] += 1
        if error_match:
            error_404 += 1

    with open(report_file, 'w') as report:
        report.write("IP Address Requests:\n")
        for ip, count in ip_requests.items():
            report.write(f"{ip}: {count}\n")

        report.write("\nPages Requested:\n")
        for page, count in pages_requested.items():
            report.write(f"{page}: {count}\n")

        report.write(f"\n404 Errors: {error_404}\n")

if __name__ == "__main__":
    analyze_logs()
