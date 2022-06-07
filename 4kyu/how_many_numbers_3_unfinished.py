# https://www.codewars.com/kata/5877e7d568909e5ff90017e6/train/python
# still too slow

import math

def find_all(sum_dig, digs):
    if sum_dig > digs*9: # it's impossible to reach the number
        return []
    
    ans = []
    lower_bound = int("1"*(digs))
    upper_bound = 10**(digs-1)*(math.ceil(sum_dig/digs)+1)
    if upper_bound < lower_bound:
        upper_bound = lower_bound + 1

    print(lower_bound, upper_bound)

    for i in range(lower_bound, upper_bound):
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


print(find_all(27, 3)) # [8, 118, 334]
# print(find_all(10, 2))
