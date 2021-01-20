
#가장첫번쨰 수 구하기
def findFirst(start,end,arr,target):
  if start>end:
    return 1e9
  mid = (start+end) // 2
  if mid == 0 :
    return 0
  
  if arr[mid] ==target  and arr[mid-1]<target:
    return mid
  elif arr[mid]==target and arr[mid-1]==target:
    return findFirst(start,mid-1,arr,target)
  
  elif arr[mid]<target:
    return findFirst(mid+1,end,arr,target)
  else:
    return findFirst(start,end-1,arr,target)
#가장 나중 수 구하기
def findLast(start,end,arr,target):
  if start>end:
    return 1e9
  if start == end :
    return n-1

  mid = (start+end) // 2

  if arr[mid] ==target  and arr[mid+1]>target:
    return mid
  elif arr[mid]==target and arr[mid+1]==target:
    return findLast(mid+1,end,arr,target)
  
  elif arr[mid]<target:
    return findLast(mid+1,end,arr,target)
  else:
    return findLast(start,end-1,arr,target)


n, x  = map(int,input().split())
arr = list(map(int,input().split()))

st = findFirst(0,n-1,arr,x)
la = findLast(0,n-1,arr,x)
if st==1e9 or la ==1e9:
  print(0) 
else:
  print(la-st+1)
