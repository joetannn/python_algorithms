#dynamic programming of fibonacci and tribonacci sequences

import time
import random
import copy

random.seed() # system time
begin = time.process_time()

maximum = 50000
arr = [0,1]
arr += [0] * (maximum - 2)
for i in range(2, maximum):
    arr[i] = arr[i - 1] + arr[i - 2]


print('Fibonacci xecution took at least ' + str(time.process_time() - begin) + ' seconds')

begin = time.process_time()

arr = [0,0,1]
arr += [0] * (maximum - 3)
for i in range(3, maximum):
    arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]


print('Tribonacci execution took at least ' + str(time.process_time() - begin) + ' seconds')
