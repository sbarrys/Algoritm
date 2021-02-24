t =int(input())
for tc in range(t):
  li=[]
 
  n,m= map(int,input().split())
  for _ in range(n):
    temp = list(map(int,input().split() ))
    li.append(temp)
  result=0
  for i in range(0,n-m+1):
    for j in range(0,n-m+1):
      temp_sum=0
       
      for box_x in range(0,m):
        for box_y in range(0,m):
          temp_sum+=li[i+box_x][j+box_y]
      result=max(temp_sum,result)
  print("#",end="")
  print(tc+1,end=" ")
  print(result)