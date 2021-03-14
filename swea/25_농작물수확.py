T = int ( input())
for testcase in range(T):
  n= int(input())
  sum=0
  li=[]
 
  for _ in range(n):
    li.append(list(map(int,input())))
 
  mid= n//2
   
  for i in range(mid+1):
    for j in range(mid-i,mid+i+1):
      sum+=li[i][j]
       
  for i in range(mid+1,n):
    for j in range( i-mid ,n-i+mid):
      sum+=li[i][j]
  print("#",end="")
  print(testcase+1,end=" ")
  print(sum)