n= int(input())
dp= [1]*(n)
li = list(map(int,input().split()))
for i in range(n):
  for j in range(0,i):
    if li[j]<li[i]:
      dp[i]= max(dp[j]+1,dp[i])
print(max(dp))