#!/usr/bin/python3

""" A script that reads stdin and retrieves specific information line by line """

import sys
import signal
from collections import defaultdict

# Initialize metrics variables
total_size = 0
status_counts = defaultdict(int)
line_count = 0

# List of valid status codes to track
valid_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

# Function to print metrics
def print_metrics():
    print(f"File size: {total_size}")
    for code in sorted(valid_status_codes):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

# Signal handler for CTRL+C to print metrics and exit gracefully
def handle_interrupt(signum, frame):
    print_metrics()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, handle_interrupt)

try:
    # Main loop to read from stdin
    for line in sys.stdin:
        parts = line.strip().split()
        
        # Validate line format (must have at least 2 parts for status code and file size)
        if len(parts) < 2:
            continue

        # Increment line count
        line_count += 1

        # Try to parse file size and status code
        try:
            file_size = int(parts[-1])          # last item
            status_code = int(parts[-2])        # second last item
            total_size += file_size             # add to total file size
            
            # Update status code count if it's a valid code
            if status_code in valid_status_codes:
                status_counts[status_code] += 1
        except (ValueError, IndexError):
            # Skip lines with unexpected format or data types
            continue

        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print_metrics()

    # Print final metrics after reading all lines
    print_metrics()

except KeyboardInterrupt:
    # Handle keyboard interrupt gracefully if signal handler fails
    print_metrics()
    sys.exit(0)
