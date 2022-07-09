r, c = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(r)]
t = int(input())

count = 0

# 3X3 필터가 가능한 시작점 범위
for a in range(r - 2):
    for b in range(c - 2):
        median = 0
        filter = []
        # 3X3 필터로 범위 설정
        for i in range(a, a + 3):
            for j in range(b, b + 3):
                filter.append(arr[i][j])
        filter.sort()

        if(filter[4] >= t):
            count += 1

print(count)