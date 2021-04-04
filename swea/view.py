for t in range(1,11):
  n =int(input())
  builds = list(map(int,input().split()))
 
  sum=0
  for i in range(2,n-2):
    a= builds[i]- max(builds[i-2],builds[i-1],builds[i+1],builds[i+2])
    if a > 0:
      sum+=a
  print("#",end="")
  print(t,end=" ")
  print(sum)