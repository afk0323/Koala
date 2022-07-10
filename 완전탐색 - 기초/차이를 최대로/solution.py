from itertools import permutations as pm

n = int(input())
nums = list(map(int, input().split()))
sum = 0

# nums의 순열의 경우들로 반복문
for ans in pm(nums):
  temp = 0
  # 모든 경우의 수를 확인
  for i in range(n-1):
    temp += abs(ans[i] - ans[i + 1])
  sum = max(sum, temp)

print(sum)