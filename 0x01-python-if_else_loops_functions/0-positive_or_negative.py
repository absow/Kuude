#!/usr/bin/python3

import random
number = random.randint(-10, 10)

if number < 0:
    print("Is negative\n")
elif number == 0:
    print("Is zero\n")
else:
    print("Is positive\n")
