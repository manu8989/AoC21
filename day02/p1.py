#!/usr/bin/env python


import os
import sys
import math


if __name__ == "__main__":
    filepath = 'input.txt'
    horizontal = 0
    depth = 0
    with open(filepath) as file:
        for line in file.readlines():
            cmd = line.split(' ')
            cmd[1] = int(cmd[1])
            if cmd[0] == "forward":
                horizontal += cmd[1]
            if cmd[0] == "up":
                depth -= cmd[1]
            if cmd[0] == "down":
                depth += cmd[1]
        
    print(horizontal*depth)