#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        print(x)
    except Exception:
        if x > my_list:
            print("The x is grater than the value")
