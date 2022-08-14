"""
Functions:
- max(list)
"""

list_1 = [-99999, -9, 89,-80, 234, -10000, 99999999]

def max(my_list):
    a = list_1[0]
    for x in my_list:
        if x >= a:
            a = x
        else:
            continue
    print(f"nilai maksimum adalah: {a}")

def min(my_list):
    a = list_1[0]
    for x in my_list:
        if x <= a:
            a = x
        else:
            continue
    print(f"nilai minimum adalah: {a}")

max(list_1)

min(list_1)