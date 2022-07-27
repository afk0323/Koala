def dfs(start):
    if len(arr) == M:
        print(*arr)
        return

    for i in range(N):
        if data[i] not in arr:
            arr.append(data[i])
            dfs(i+1)
            arr.pop()

N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
arr = []

dfs(0)