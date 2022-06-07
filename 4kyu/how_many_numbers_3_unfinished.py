# https://www.codewars.com/kata/5877e7d568909e5ff90017e6/train/python
# still too slow

import math


def find_all(sum_dig, digs):
    if sum_dig > digs*9: # it's impossible to reach the number
        return []
    if sum_dig < digs:
        return []
    
    ans = []
    lower_bound = int("1"*(digs))
    upper_bound = int(str(math.ceil(sum_dig/digs))*digs)

    if upper_bound < lower_bound:
        upper_bound = lower_bound

    print(lower_bound, upper_bound)

    for i in range(lower_bound, upper_bound + 1):
        if digits_ascending(i):
            val = sum(int(x) for x in str(i))
            if val == sum_dig:
                ans.append(i)

    # for each digit, it increments from the previous
    # so set 1 initially, then loop from 1 to 9
    # if its 2, loop from 2 to 9

    # do a custom range using iter (things using yield thingy)
    # the yeild thing can be in functions without needing a class.
    # needs lower_bound, upper_bound.
    # give it how many digits it is and start value. 
    # Then in the for loop, if sum(digits) > num, break
    print(ans)
    if ans:
        return [len(ans), ans[0], ans[-1]]
    else:
        return []
    
def digits_ascending(num: int) -> bool:
    return str(num) == ''.join(sorted(str(num)))


print(find_all(30, 5)) # [8, 118, 334]
# print(find_all(10, 2))

'''
11111
30 - 5 = 25 >= 9
11119
30 - 13 = 17 >= 9
11199
30 - 21 = 9 >= 9
11999
30 - 29 = 1
12999
'''

