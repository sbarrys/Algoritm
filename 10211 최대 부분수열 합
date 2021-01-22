n= int(input())
for _ in range(n):
  k = int(input())
  dp=[0 for _ in range(k)]
  arr = list(map(int,input().split()))

  dp[0]=arr[0]
  for i in range(1,k):
    dp[i]= max(dp[i-1]+arr[i],arr[i])
  
  print(max(dp))