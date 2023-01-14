# Brainfuck interpreter made in Desmos graphing calculator
# https://www.desmos.com/calculator/sfjibaru0n
# This is a python script that converts bf code to the numbers used in Desmos

import re

CODE_MAP = {"+": 0, "-": 1, ">": 2, "<": 3, ".": 4, ",": 5, "[": 6, "]": 7}

with open(f"test.bf", "r") as f:
    code = f.read()

code = re.sub("[^><\+-\.,\[\]]", "", code)

out = "["
for char in code:
    out += str(CODE_MAP[char]) + ","
out += "]"

print(out)
