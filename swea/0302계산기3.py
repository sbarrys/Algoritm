icp = {')':-1 , '*':2, '+':1,'(':3}
isp = {')':-1, '*':2, '+':1, '(':3}
operator={
  '+': ( lambda a,b : a+b),
  '*': ( lambda a,b : a*b)
}

def get_postfix(formular):
  postfix= ''
  for char in formular:
    if char.isdigit():
      postfix += char  # 숫자면 출력


    elif char == ')':
      if stack:
        while stack[-1] != '(':
          postfix += stack.pop()
        stack.pop()
    else:
      if not stack or icp.get(char) > isp.get(stack[-1]):
        stack.append(char)
      else:
        while stack and icp[char] <= isp[stack[-1]]:
          a= stack.pop()
          postfix += stack.pop()
        stack.append(char)
    print(postfix, stack)
  return postfix

def get_cal(formula):
  for char in formular:
    if char.isdigit():
      stack.append(char)
    else:
      print(stack)
      b= int(stack.pop())
      a= int(stack.pop())
      stack.append(operator[char](a,b))
  return stack.pop()
for t in range(1,11):
  N= int(input())
  formular= input()
  stack=[]
  post_formula = get_postfix(formular)
  ans = get_cal(post_formula)
  print('#%d %d' %(t,ans))