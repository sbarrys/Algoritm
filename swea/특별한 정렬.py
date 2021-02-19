t=  int(input())
 
for tc  in range(t):
  n= int(input())
 
  li = list(map(int,input().split()))
  li_ = sorted(li)
  result=[]
  if n%2==0:
    for  i in range(n//2):
      result.append(li_[-1*i -1])
      result.append(li_[i])
  else:
    for  i in range(n//2):
      result.append(li_[-1*i -1])
      result.append(li_[i])
    result.append(li_[n//2])
  print("#",end="")
  print(tc+1,end=" ")
  cnt=0
  for a in result:
    cnt+=1
    if cnt==10:
      print(a,end="")
      break
    print(a,end=" ")
  print("")