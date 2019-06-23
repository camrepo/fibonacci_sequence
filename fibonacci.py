def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-2) + fib(n-1)


'''
import time

start = time.time()
fib(40)
elapsed_time = time.time() - start
'''