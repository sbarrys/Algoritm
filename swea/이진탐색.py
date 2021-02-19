t=  int(input())
 
def binary_search(target,start,end,cnt):
  mid  = (start+end)//2
  if start>end:
    return -1
  else:
    if mid == target:
      return cnt
    else:
      if mid>target:
        end=mid-1
      else:
        start= mid+1
 
  return binary_search(target, start, end, cnt+1)
 
for tc  in range(t):
  book , a, b= map(int,input().split())
  start = 0 
  end =book
  A= binary_search(a,1,book,0)
  B= binary_search(b,1,book,0)
  if A==B:
    result="0"
  elif A>B:
    result = "B"
  else:
    result = "A"
 
 
  print("#",end="")
  print(tc+1,end=" ")
  print(result)