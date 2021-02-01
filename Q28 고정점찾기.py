

def binary_search(s,e,arr):
  if s>e:
    return None
  mid = (s+e)//2
  
  if arr[mid] == mid:
    return mid
  elif arr[mid]>mid:
    return binary_search(s,mid-1,arr)
  else:
    return binary_search(mid+1,e,arr)

n= int(input())
arr = list(map(int,input().split()))

ans =(binary_search(0,len(arr),arr))
if ans==None:
  print(-1)
else:
  print(ans)