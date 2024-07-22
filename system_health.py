#!/usr/bin/env python3
import psutil
import shutil
import logging

# Configure logging
logging.basicConfig(filename='system_health.log', level=logging.INFO)

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

def check_cpu():
    usage = psutil.cpu_percent(interval=1)
    if usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage detected: {usage}%")

def check_memory():
    usage = psutil.virtual_memory().percent
    if usage > MEMORY_THRESHOLD:
        logging.warning(f"High Memory usage detected: {usage}%")

def check_disk():
    usage = shutil.disk_usage("/").percent
    if usage > DISK_THRESHOLD:
        logging.warning(f"High Disk usage detected: {usage}%")

def check_processes():
    processes = [p.info for p in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent'])]
    for process in processes:
        if process['cpu_percent'] > CPU_THRESHOLD:
            logging.warning(f"High CPU process detected: {process}")

if __name__ == "__main__":
    check_cpu()
    check_memory()
    check_disk()
    check_processes()
