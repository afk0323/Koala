n, m = map(int, input().split())
arr = [str(input()) for i in range(n)]
count = []

# 8X8 체스판이 가능한 시작점 범위
for a in range(n - 7):
    for b in range(m - 7):
        idx1 = 0
        idx2 = 0
        # 8X8 체스판으로 범위 설정
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                # 체스판의 짝수칸 / 홀수칸은 같은 색을 가진다
                if (i + j) % 2 == 0:  # 짝수
                    if arr[i][j] != 'W':
                        idx1 += 1
                    if arr[i][j] != 'B':
                        idx2 += 1
                else:  # 홀수
                    if arr[i][j] != 'B':
                        idx1 += 1
                    if arr[i][j] != 'W':
                        idx2 += 1

        print(idx1, idx2)
        count.append(min(idx1, idx2))

print(min(count))