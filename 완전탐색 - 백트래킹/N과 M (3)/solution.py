def dfs(start):
    if len(arr) == M:
        print(*arr)
        return

    for i in range(1, N+1):
            arr.append(i)
            dfs(i+1)
            arr.pop()

N, M = map(int, input().split())
arr = []

dfs(1)