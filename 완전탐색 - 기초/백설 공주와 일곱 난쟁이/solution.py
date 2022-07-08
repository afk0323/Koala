arr = [int(input()) for i in range(9)]
for a in range(9):
	for b in range(a+1, 9):
		if sum(arr) - arr[a] - arr[b] == 100:
			for i in range(9):
				# if i != a or i != b:
				if i not in [a, b]:
					print(arr[i])