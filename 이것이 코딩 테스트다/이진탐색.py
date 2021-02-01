def binary_search(array,target,start,end):
  while start <= end:
    mid = (start + end) //2
    if array[mid] == target:
      return mid
    if array[mid]>target:
      end = mid-1
    else:
      start= mid+1

  return None

n,target =map(int,input().split())

arr = list(map(int,input().split()))

result = binary_search(arr,target,0,n-1)

if result==None:
  print("원소 x")
else:
  print(result+1,"에 있습니다.")