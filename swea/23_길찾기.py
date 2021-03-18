for t in range(1, 11):
    tc, N = map(int, input().split())
    arr = [[] for _ in range(100)]
    D = list(map(int, input().split()))
 
    for i in range(N):
        arr[D[2*i]].append(D[2*i + 1])
 
 
    stack = [0]
    visited = [0] * 100
    result = 0
 
    while len(stack):
        node = stack.pop()
        if not visited[node]:
            visited[node] = 1
            for n in arr[node]:
                if not visited[n]:
                    stack.append(n)
 
    if visited[99]:
        print('#%d 1' %t)
    else:
        print('#%d 0' %t)