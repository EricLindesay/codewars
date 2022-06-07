# https://www.codewars.com/kata/5877e7d568909e5ff90017e6/train/python
# still too slow

import math

from sklearn import multiclass

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

    # don't use a for loop. Since we know the numbers must be ascending
    # we can skip a large portion of them.
    # Do it recursively and you don't need digits_ascending
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


print(find_all(3, 4)) # [8, 118, 334]
# print(find_all(10, 2))
