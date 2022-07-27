def playerAbility(idx, num):
    global res

    # 팀을 모두 구했으면 점수를 계산한다
    if num == n // 2:
        aTeam, bTeam = 0, 0
        for i in range(n):
            for j in range(i+1, n):
                # 두 선수가 같은 팀인지 확인하고, 같은 팀이면 점수를 부여한다
                if team[i] == team[j]:
                    if team[i] == 0: aTeam += arr[i][j] + arr[j][i]
                    else: bTeam += arr[i][j] + arr[j][i]
        # 팀 점수의 차이가 res보다 작은 지 확인한다
        res = min(res, abs(aTeam - bTeam))
        return  # 탐색종료

    # 팀을 정하는 for문
    for i in range(idx+1, n):
        team[i] = 1
        # 재귀함수를 통해서, i가 B팀에 속한 모든 경우의 수를 확인한다
        playerAbility(i, num + 1)
        # 그 후에 i를 A팀으로 바꾼다
        team[i] = 0


n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]
res = float('inf') # 무한대
team = [0] * n
playerAbility(0, 0)
print(res)