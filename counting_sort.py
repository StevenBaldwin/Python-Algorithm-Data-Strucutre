import random


def counting_sort(arr):
    output_arr = [0]*len(arr)
    count_arr = [0]*100

    for i in arr:
        count_arr[i]+=1
    for i in range(1,len(count_arr)):
        count_arr[i]+=count_arr[i-1]
    for i in arr:
        output_arr[count_arr[i]-1] = i
        count_arr[i]-=1
    return output_arr        

def test_count_sort():
    for i in range(20):
        a = [random.randint(1,99) for i in range(50)]
        b = sorted(a)
        if counting_sort(a) == b:
            print(True)



test_count_sort()
