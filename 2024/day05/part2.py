
import sys
from collections import defaultdict

rules = []
updates  = []

rules_section, update_section = sys.stdin.read().strip().split("\n\n")
for line in rules_section.splitlines():
    x,y = map(int, line.split("|"))
    rules.append((x,y))


for line in update_section.splitlines():
    updates.append(list(map(int, line.split(","))))


def isValid(rules, update_line):

    for before,after in rules:
        if before in update_line and after in update_line:
            if update_line.index(before) > update_line.index(after):
                return False
    return True


def func(rules, updates):
    
    ans = 0
    for update_line in updates:
        if isValid(rules, update_line):
            ans += update_line[len(update_line) // 2]
    return ans

print(func(rules, updates))

