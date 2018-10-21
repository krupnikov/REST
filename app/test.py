import time
import random

# time.sleep(random.randint(0, 10))

def main():
    str_time = time.time()
    time.sleep(random.randint(0, 10))
    executable_time = (time.time() - str_time)
    return executable_time

if __name__ == '__main__':
    main()
