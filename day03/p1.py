#!/usr/bin/env python


import os
import sys
import math


if __name__ == "__main__":
    filepath = 'input.txt'
    gamma = ""
    epsilon = ""
    with open(filepath) as file:
        lines = [l.strip() for l in file.readlines()]
        for i in range(len(lines[0])):
            if sum(int(l[i]) for l in lines) > len(lines)/2:
                gamma += "1"
                epsilon += "0"
            else:
                gamma += "0"
                epsilon += "1"
    
    print(int(gamma,2)*int(epsilon,2))