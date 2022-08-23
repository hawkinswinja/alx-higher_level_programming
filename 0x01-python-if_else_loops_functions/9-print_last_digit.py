#!/usr/bin/python3
def print_last_digit(number):
    "return and print the last digit of number"
    number = abs(number) % 10
    print(f"{number}", end='')
    return number
