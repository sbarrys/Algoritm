n = int(input())

s= list(map(int,input().split()))
switch =[0]
for s_n in s:
  switch.append(s_n)

sex_idx=[]
people = int(input())
for _ in range( people):
  a,b = map(int,input().split())
  sex_idx.append((a,b))

for sex,idx in sex_idx:
  if sex==1:
    first_idx = idx
    while 1:
      if idx <len(switch):

        switch[idx]  = (switch[idx]+1)%2
        idx+=first_idx
      else:
        break
  if sex ==2:
    switch[idx]  = (switch[idx]+1)%2

    if 1<idx<len(switch):
      
      pre=  idx-1
      nxt=  idx+1
      while pre>0 and nxt <len(switch):

        if switch[pre]==switch[nxt]:

          switch[pre]  = (switch[pre]+1)%2
          switch[nxt]  = (switch[nxt]+1)%2
          pre-=1
          nxt+=1

        else:
          break
line=0
for n in switch[1:]:
  print(n,end=" ")
  line+=1
  if line%20==0:
    print()
