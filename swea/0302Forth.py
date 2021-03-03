op = {'+', '-', '*', '/'}
T = int(input())
for t in range(1, T+1):
    N = list(input().split())
    stack = []
    result = 0
    for i in N:
        if i == '.':
            if len(stack) > 1:
                result = 'error'
            else:
                result = str(stack.pop())
        elif i not in op:
            stack.append(int(i))
        else:
            if len(stack) < 2:
                result = 'error'
                break
            else:
                B = stack.pop()
                A = stack.pop()
                if i == '+':
                    stack.append(A + B)
                elif i == '-':
                    stack.append(A - B)
                elif i == '*':
                    stack.append(A * B)
                else:
                    stack.append(int(A / B))
    print('#%d %s' % (t, result))