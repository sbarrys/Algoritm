for t in range(10):
  n= int(input())
  stk=[]
  flag=True
  moem=list(map(str,input()))
  for i in range(n):
    if not stk:
      stk.append(moem[i])
      continue
    else:
      top_stk= stk.pop()
      if moem[i] == ']' :
        if top_stk=='[':
          top_stk=''
          continue
        else:
          print("#",end="")
          print(t+1,end=" ")
          print('0')
          flag=False
          break

      elif moem[i]=='}' :
        if top_stk=='{':
          continue
        else:
          print("#",end="")
          print(t+1,end=" ")

          print('0')
          flag=False
          break
      elif moem[i]=='>':
        if top_stk=='<':
          continue
        else:
          print("#",end="")
          print(t+1,end=" ")

          print('0')
          flag=False
          break
      elif moem[i]==')':
        if top_stk=='(':
          continue
        else:
          print("#",end="")
          print(t+1,end=" ")

          print('0')
          flag=False
          break
      else:
        stk.append(top_stk)
        stk.append(moem[i])
  if flag:
    print("#",end="")
    print(t+1,end=" ")
    print("1")
