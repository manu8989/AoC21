#!/usr/bin/env python


import os
import sys
import math


if __name__ == "__main__":
    filepath = 'input.txt'
    solution = 0
    with open(filepath) as file:
        lines = [int(l) for l in file.readlines()]
        last_line = lines[0]
        for line in lines[1:]:
            if line > last_line:
                solution += 1
            last_line = line
        
    print(solution)