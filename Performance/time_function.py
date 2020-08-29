import random
import time
a1, a2 = [], []


def setup(n):
    global a1, a2
    a1 = random.sample(range(0, 2*n), n)
    a2 = random.sample(range(0, 2 * n), n)


def common_items():

    common = []
    for item in a1:
        if item in a2:
            common.append(item)


if __name__ == "__main__":

    # Time the function with input of size 100 elements
    setup(100)
    list_time = []
    for i in range(10):
        start = time.time()
        common_items()
        end = time.time()
        list_time.append(end - start)
    print(sum(list_time)/(len(list_time)))

    # Time the function with input of size 1000 elements
    setup(1000)
    for i in range(10):
        start = time.time()
        common_items()
        end = time.time()
        list_time.append(end - start)
    print(sum(list_time)/(len(list_time)))

    # Time the function with input of size 10000 elements
    setup(10000)
    for i in range(10):
        start = time.time()
        common_items()
        end = time.time()
        list_time.append(end - start)
    print(sum(list_time)/(len(list_time)))