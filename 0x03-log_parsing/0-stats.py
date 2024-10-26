#!/usr/bin/python3

""" a script that reads stdin and retrieves specific information line by line"""

import sys


def print_metrics(code, size):
    """prints the retrieved information"""
    print("File size: {:d}".format(size))
    for i in sorted(code.keys()):
        if code[i] != 0:
            print("{}: {:d}".format(i, code[i]))

    accepted_code = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

    count = 0
    size = 0

    try:
        for line in sys.stdin:
            if count != 0 and count % 10 == 0:
                print_metrics(accepted_code, size)

            parts = line.split()
            count += 1

            try:
                size += int(parts[-1])
            except:
                pass

            try:
                if parts[-2] in accepted_code:
                    accepted_code[parts[-2]] += 1
            except:
                pass
        print_metrics(accepted_code, size)

    except Keyboardinterrupt:
        print_metrics(accepted_code, size)
        raise
