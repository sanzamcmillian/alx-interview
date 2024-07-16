#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""
import sys
import signal


total_file_size = 0
status_code_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}


def print_metrics():
    """function to print metrics"""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")



def signal_handler(sig, frame):
    """signal handler for keyboard interruptions"""
    print_metrics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
line_count = 0

for line in sys.stdin:
    line_count += 1
    parts = line.split()
    
    if len(parts) >= 0:
        try:
            file_size = int(parts[-1])
            status_code = parts[-2]
            
            total_file_size  += file_size
            if status_code in status_code_count:
                status_code_count[status_code] += 1
        except ValueError:
            pass
        
    if line_count % 10 == 0:
        print_metrics()

print_metrics()
