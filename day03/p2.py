#!/usr/bin/env python


import os
import sys
import math

def filter_lines(lines, begin):
    result = []
    for l in lines:
        if l.startswith(begin):
            result.append(l)
    return result

def solve(lines, significant_one):
    result = ""
    for i in range(len(lines[0])):
        if sum(int(l[i]) for l in lines) >= len(lines)/2.0:
            result += "1" if significant_one else "0"
        else:
            result += "0" if significant_one else "1"
        lines = filter_lines(lines, result)
        if(len(lines) == 1):
            result = lines[0]
            break
    return result

if __name__ == "__main__":
    filepath = 'input.txt'
    with open(filepath) as file:
        lines = [l.strip() for l in file.readlines()]
        oxy = solve(lines, True)
        co2 = solve(lines, False)
    
        print(int(oxy,2)*int(co2,2))