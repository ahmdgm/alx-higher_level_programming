#!/usr/bin/python3
def max_integer(my_list=[]):
    my_list_len = len(my_list)
    if my_list_len == 0:
        return "None"
    else:
        a = my_list[0]
        for i in range (my_list_len)
            if a < my_list[i]:
                a = my_list[i]
        return a
