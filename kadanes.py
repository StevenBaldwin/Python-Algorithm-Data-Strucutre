from random import randint

def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far



for i in range(100):
    p = [randint(-10**2,10**2) for x in range(1000)]
    print(p)
    print(max_subarray(p))
