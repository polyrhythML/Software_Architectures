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


def test_function():

    list_time = []
    for _ in range(10):
        start = time.time()
        common_items()
        end = time.time()
        list_time.append(end - start)
    return sum(list_time)/(len(list_time))


if __name__ == "__main__":

    # Time the function with input of size 100 elements
    setup(100)
    val = test_function()
    print(val)

    # Time the function with input of size 1000 elements
    setup(1000)
    val = test_function()
    print(val)

    # Time the function with input of size 10000 elements
    setup(10000)
    val = test_function()
    print(val)
