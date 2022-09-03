#!/usr/bin/python3


if __name__ == "__main__":
    import sys
print(f"{len(sys.argv) -1} argument:")
arguments = len(sys.argv) - 1
position = 1
while (arguments >= position):
    print("%i: %s" % (position, sys.argv[position]))
    position = position + 1

