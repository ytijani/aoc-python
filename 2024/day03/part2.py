import re
import sys

text  = sys.stdin.read()
pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
matches = re.finditer(pattern, text)


enabled = True
total = 0
for match in matches:
    word = match.group(0)

    if word == 'do()':
        enabled = True
    elif word == "don't()":
        enabled = False
    else:
        if enabled:
            total += int(match.group(1)) * int(match.group(2))

print(total)
