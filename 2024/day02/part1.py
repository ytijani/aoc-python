
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


def func(reports):

    return sum(is_safe(line) for line in reports)

print(func(reports))
