T = int(input())
for t in range(1, T+1):
    N = int(input())
    price_list = list(map(int, input().split()))
    stack = [price_list[N-1]]
    result = 0
    for i in range(N-2, -1, -1):
        if stack[-1] < price_list[i]:
            stack.append(price_list[i])
        else:
            result += stack[-1] - price_list[i]
 
    print('#%d %d' %(t, result))