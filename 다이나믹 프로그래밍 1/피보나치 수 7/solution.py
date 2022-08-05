MOD = 10**9 + 7

n = int(input())
fibo = [0, 1]
if n in [0, 1]:
    print(fibo[n])
    exit()

for i in range(2, n+1):
    fibo = [fibo[1], (fibo[0] + fibo[1]) % MOD]

print(fibo[1])