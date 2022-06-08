# https://www.codewars.com/kata/5877e7d568909e5ff90017e6/train/python
# still too slow

import math


def find_all(sum_dig, digs):
    if sum_dig > digs*9: # it's impossible to reach the number
        return []
    if sum_dig < digs:
        return []
    
    ans = []
    lower_bound = "9"*((sum_dig-digs)//8)  # add in as many 9s as are allowed
    if len(lower_bound) < digs:
        lower_bound = str((sum_dig-digs)%8 + 1) + lower_bound  # use the remaining values to overflow into the earlier digits
    lower_bound = "1"*(digs-len(lower_bound)) + lower_bound  # add in leading 1s
    lower_bound = int(lower_bound)  # convert to int

    num_divisible = math.ceil(sum_dig/digs)
    to_change = (num_divisible*digs)%sum_dig  # number of digits you need to reduce by one
    if to_change < digs:
        upper_bound = str(num_divisible-1)*to_change  # add on the reduced digits
    upper_bound += str(num_divisible)*(digs-len(upper_bound))  # add on the rest of the digits to get it to the right length
    upper_bound = int(upper_bound)  # convert to int

    print(lower_bound, upper_bound)

    for i in range(lower_bound, upper_bound + 1):
        if digits_ascending(i):
            val = sum(int(x) for x in str(i))
            if val == sum_dig:
                ans.append(i)

    if ans:
        return [len(ans), ans[0], ans[-1]]
    else:
        return []
    
def digits_ascending(num: int) -> bool:
    return str(num) == ''.join(sorted(str(num)))


print(find_all(40, 7))
