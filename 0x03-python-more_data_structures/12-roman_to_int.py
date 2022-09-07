#!/usr/bin/python3
# https://cdn1.byjus.com/wp-content/uploads/2020/11/Roman-Numerals-chart.png
def roman_to_int(roman_string):
    if roman_string == "I":
        return 1
    if roman_string == "V":
        return 5
    if roman_string == "X":
        return 10
    if roman_string == "L":
        return 50
    if roman_string == "D":
        return 500
    return 0

print(roman_to_int("I"))
print(roman_to_int("V"))
print(roman_to_int("X"))
print(roman_to_int("L"))
print(roman_to_int("D"))

print(roman_to_int("II"))
print(roman_to_int("III"))
print(roman_to_int("IV"))
print(roman_to_int("V"))
print(roman_to_int("VI"))
