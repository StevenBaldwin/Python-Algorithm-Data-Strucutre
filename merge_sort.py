from random import randint

def merge(x):
    if len(x) == 1:
        return x
    else:
        mid = int(len(x) / 2)
        l = merge(x[:mid])
        r = merge(x[mid:])
    i = j = 0
    result = []
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    result += l[i:]
    result += r[j:]
    return result


def tester():
    for _ in range(10):
        l = [randint(-2**30,2**30) for x in range(3000)]
        correct = sorted(l) == merge(l)
        if not correct:
            print("FAIL")
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
