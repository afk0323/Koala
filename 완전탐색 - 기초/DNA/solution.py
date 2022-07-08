n, m = map(int, input().split())
arr = [str(input()) for i in range(n)]

result = ''
count = 0

for i in range(m):
    DNA = [0, 0, 0, 0]  # A,T,G,C

    # n개의 DNA 중에서 가장 많이 나온 뉴클레오티드 구하기
    for j in range(n):
        if arr[j][i] == 'A':
            DNA[0] += 1
        elif arr[j][i] == 'C':
            DNA[1] += 1
        elif arr[j][i] == 'G':
            DNA[2] += 1
        elif arr[j][i] == 'T':
            DNA[3] += 1

    idx = DNA.index(max(DNA))

    # Hamming Distance의 합이 가장 작은 DNA 구하기
    if idx == 0:
        result += 'A'
    elif idx == 1:
        result += 'C'
    elif idx == 2:
        result += 'G'
    elif idx == 3:
        result += 'T'

    # Hamming Distance 계산하기
    count += n - max(DNA)

print(result)
print(count)