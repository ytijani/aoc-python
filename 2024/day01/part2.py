



import sys
from collections import Counter

list1 = []
list2 = []

for line in sys.stdin:
    val1, val2 = line.split()
    list1.append(int(val1))
    list2.append(int(val2))




def calculate_distance_between_lists(list1, list2):

    count_list2 = Counter(list2)
    ans = 0
    for i in range(len(list1)):
        ans +=  list1[i] * count_list2[list1[i]]
    return ans





print(calculate_distance_between_lists(list1, list2))
