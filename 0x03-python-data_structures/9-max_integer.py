#!/usr/bin/python3
def max_integer(my_list=[]):
    my_list_len = len(my_list)
    if my_list_len == 0:
        return "None"
    for i in range (my_list_len):
        a = my_list[0]
        if a < my_list[i]:
            a = my_list[i]
    return a
