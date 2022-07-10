from itertools import permutations as pm

n = int(input())

for i in range(n):
    dots = int(input())
    arr = [*map(int, input().split())]
    arr.sort()

    count = 0

    for ans in pm(arr, 3):
        if abs(ans[0] - ans[1]) == abs(ans[2] - ans[1]):
            count += 1

    print(int(count/2))