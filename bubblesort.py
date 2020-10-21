import time
import random
import copy

random.seed() # system time

orig = [random.randrange(-10000, 10000) for i in range(5000)] #random array
x = copy.deepcopy(orig)

begin = time.process_time()

#bubble sort
for i in range(len(x) - 1):
    for j in range(len(x) - i - 1):
        if x[j] > x[j + 1]:
            x[j], x[j + 1] = x[j + 1], x[j]

print('Execution took at least ' + str(time.process_time() - begin) + ' seconds')
