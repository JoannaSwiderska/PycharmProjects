import time
import random

def log_time(func):
    def inner():
        start = time.time()
        x = func()
        end = time.time() - start
        print(f'czas dzialania {end}')
        return x
    return inner

# dekorujemy funkcje zeby sie bezposrednio odwolac pozniej w body programu
@log_time
def foo():
    val = random.randint(1, 5)
    print('before sleep')
    time.sleep(val)
    print('after sleep')

# start = time.time()
# foo()
# end = time.time() - start
# print(f'czas dzialania {end}')

if __name__ == '__main__':
    # log_time(foo)
    # log_time(foo)
    # log_time(foo)
    foo()