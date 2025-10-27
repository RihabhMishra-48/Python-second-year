# Take as input N, the size of an array. Take N more inputs and store that in an array. Take another number’s
# input as M. Write a function which returns the index on which M is found in an array, in case M is not
# found -1 is returned. Print the value returned.

N = int(input("Enter the number of elements: "))
arr = list(map(int, input().split()))

M = int(input("Enter the number to check: "))

def find_index(arr, M):
    for i in range(len(arr)):
        if arr[i] == M:
            return i
    return -1

print(find_index(arr, M))
