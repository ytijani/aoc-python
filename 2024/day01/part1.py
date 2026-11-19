



import sys


list1 = []
list2 = []

for line in sys.stdin:
    val1, val2 = line.split()
    list1.append(int(val1))
    list2.append(int(val2))




def calculate_distance_between_lists(list1, list2):

    list1.sort()
    list2.sort()

    ans = 0
    for i in range(len(list1)):
        ans +=  abs(list1[i] - list2[i])
    return ans





print(calculate_distance_between_lists(list1, list2))
