for tc in range(1, 1 + int(input())):
  li = list(input())
  stack = []
  while li:
    a = li.pop()
    if not stack:
      stack.append(a)
    elif a == stack[-1]:
      stack.pop()
    else:
      stack.append(a)
  print('#{} {}'.format(tc, len(stack)))