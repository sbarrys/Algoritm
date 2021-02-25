nums = [i for i in range(1, 13)]
n = len(nums)
 
T = int(input())
 
for t in range(1, T+1):
    N, K = map(int, input().split())
    cnt = 0
    for i in range(1 << n):
        total = 0
        length = 0
        for j in range(n):
            if i & (1 << j):
                total += nums[j]
                length += 1
 
        if length == N and total == K:
            cnt += 1
 
    print('#%d %d' % (t, cnt))