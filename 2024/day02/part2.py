
import sys


reports = [
    list(map(int, line.split()))
    for line in sys.stdin
]




def is_safe(line):

    diffs = [
        line[i] - line[i - 1]
        for i in range(1, len(line))
    ]


    return all( 1 <= d <= 3 for d in diffs) or all(-3 <= d <= -1 for d in diffs)

def is_safe_dampened(line):

    if is_safe(line):
        return True

    for i in range(len(line)):
        new_line = line[:i] + line[i + 1:]
        if is_safe(new_line):
            return True
    return False


def func(reports):

    return sum(is_safe_dampened(line) for line in reports)

print(func(reports))
