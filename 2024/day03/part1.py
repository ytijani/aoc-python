import re
import sys

text  = sys.stdin.read()
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

matches = re.findall(pattern, text)

total = 0

for x,y in matches:
    total += int(x) * int(y)

print(total)
