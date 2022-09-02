#!/usr/bin/python3

import sys

if __name__ == "__main__":
    print(f"Arguments: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i}: {arg}")



