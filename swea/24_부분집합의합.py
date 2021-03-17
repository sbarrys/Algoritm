def bubun(i):
    global res
    if i == N:
        cnt = 0
        sel_sum = 0
        for j in range(M):
            if selec[j]:
                cnt += 1
                sel_sum += j + 1
        if cnt == N and sel_sum == K:
            res += 1
        return
 
    selec[i] = 1
    bubun(i+1)
    selec[i] = 0
    bubun(i+1)
 
 
T = int(input())
 
M = 12
for tc in range(1, T+1):
    N, K = map(int, input().split())
    selec = [0] * M
 
    res = 0
    bubun(0)
 
    print('#%d %d' % (tc, res))