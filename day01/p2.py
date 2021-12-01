#!/usr/bin/env python


import os
import sys
import math


if __name__ == "__main__":
    filepath = 'input.txt'
    solution = 0
    with open(filepath) as file:
        lines = [int(l) for l in file.readlines()]
        i = 1
        last_sum = sum(lines[0:3])
        while len(lines[i:i+3]) == 3:
            current_sum = sum(lines[i:i+3])
            if current_sum > last_sum:
                solution += 1
            last_sum = current_sum
            i += 1
        
    print(solution)