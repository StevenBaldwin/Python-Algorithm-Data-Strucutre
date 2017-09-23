from random import randint
import sys

def quick_sort(arr):

    if len(arr) > 1:
        l = []
        eq = []
        h = []
        random_pivot = arr[randint(0,len(arr)-1)]
        for x in arr:
            if x < random_pivot:
                l.append(x)
            elif x == random_pivot:
                eq.append(x)
            else:
                h.append(x)
        return quick_sort(l) + eq + quick_sort(h)
    else:
        return arr


def tester():
    for _ in range(10):
        rand_list = [randint(-2**45,2**45) for x in range(10000)]
        if (quick_sort(rand_list) != sorted(rand_list)):
            print("FAILED :(")
            sys.exit(0)
    print("""
  _____                _____    _____   ______   _____        _     _     _
 |  __ \      /\      / ____|  / ____| |  ____| |  __ \      | |   | |   | |
 | |__) |    /  \    | (___   | (___   | |__    | |  | |     | |   | |   | |
 |  ___/    / /\ \    \___ \   \___ \  |  __|   | |  | |     | |   | |   | |
 | |       / ____ \   ____) |  ____) | | |____  | |__| |     |_|   |_|   |_|
 |_|      /_/    \_\ |_____/  |_____/  |______| |_____/      (_)   (_)   (_)
""")


tester()
