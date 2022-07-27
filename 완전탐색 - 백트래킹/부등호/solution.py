def inequalitySign(idx):
    global minAns, maxAns
    # 값을 비교해서 minAns나 maxAns에 넣어준다
    if idx == n:
        val = ''.join(map(str, ans))
        if minAns[0] > int(val): minAns = [int(val), val]
        if maxAns[0] < int(val): maxAns = [int(val), val]
        return
    for i in range(10):
        if i not in ans:
            # 부등호대로 값을 넣을 수 있는 지 확인
            if (s[idx] == '<' and ans[-1] < i) or (s[idx] == '>' and ans[-1] > i):
                ans.append(i)
                inequalitySign(idx + 1)
                ans.pop()


n = int(input())
s = input().split()
ans = []
minAns = [float('inf'), '']
maxAns = [0, '']
# 재귀적으로 inequalitySign 함수를 실행한다
for i in range(10):
    ans.append(i)
    inequalitySign(0)
    ans.pop()
print(maxAns[1])
print(minAns[1])