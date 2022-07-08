from itertools import permutations as pm
n = int(input())
arr = [i+1 for i in range(n)]
for ans in pm(arr):
	print(*ans)