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

''' elapled_time = 6.6e-5 [esc.]

from functools import lru_cache
@lru_cache(maxsize=None)
def fib_cache(n):
    if n < 2:
        return n
    else:
        return fib_cache(n-2) + fib_cache(n-1)
        
'''