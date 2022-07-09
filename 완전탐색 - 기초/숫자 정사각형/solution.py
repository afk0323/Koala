n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input())))

num = min(n, m)  # 가질 수 있는 최대 크기의 제곱근
size = 1

for i in range(n):
    for j in range(m):
        for k in range(1, num):
            # N X M 범위를 넘지 않을 때
            if i + k < n and j + k < m:
                vertex = arr[i][j]
                if vertex == arr[i+k][j] and vertex == arr[i][j+k] and vertex == arr[i+k][j+k]:
                    size = max(size, (k + 1)**2)

print(size)