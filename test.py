import time
import random

def main():
    start_time = time.clock()
    time.sleep(random.randint(0, 10))
    executable_time = (time.time() - start_time)
    return start_time, executable_time

if __name__ == '__main__':
    print(main())
