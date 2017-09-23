import sys
import random,string
# RUNTIME O(N)
# http://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/
def kmp(pattern, txt):
    match_positions = []
    M = len(pattern)
    N = len(txt)
    lps = [0]*M

    compute_lps_arr(pattern,lps)
    i,j=0,0

    while i < N:
        if pattern[j]==txt[i]:
            j+=1
            i+=1

        if j==M:
            match_positions.append(i-j)
            j = lps[j-1]

        elif i < N and pattern[j] != txt[i]:
            if j!=0:
                j = lps[j-1]
            else:
                i+=1
    return match_positions

def compute_lps_arr(pattern,lps):
    length = 0
    M = len(pattern)
    i=1

    while i<M:
        if pattern[i] == pattern[length]:
            length+=1
            lps[i]=length
            i+=1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i]=0
                i+=1


def print_pass():
    print("""
 _____                _____    _____   ______   _____        _     _     _
|  __ \      /\      / ____|  / ____| |  ____| |  __ \      | |   | |   | |
| |__) |    /  \    | (___   | (___   | |__    | |  | |     | |   | |   | |
|  ___/    / /\ \    \___ \   \___ \  |  __|   | |  | |     | |   | |   | |
| |       / ____ \   ____) |  ____) | | |____  | |__| |     |_|   |_|   |_|
|_|      /_/    \_\ |_____/  |_____/  |______| |_____/      (_)   (_)   (_)
""")



def tester():
    f = open("kmp_test.in",'r')
    while True:
        for _ in range(3):
            pattern = str(f.readline()).rstrip()
            if '#' in pattern:
                print_pass()
                sys.exit(0)
            txt = str(f.readline()).rstrip()
            positions = eval(f.readline())
            if kmp(pattern,txt) != positions:
                print("FAIL")
                sys.exit(0)

tester()
