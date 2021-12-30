from collections import deque

def solution(n, edge):
    answer = 0
    graph = {n:set() for n in range(1,n+1)}
    for item in edge:
        graph[item[0]].add(item[1])
        graph[item[1]].add(item[0])
    
    stack = deque([])
    visited = set()
    visited.add(1)
    stack.append((1,0))
    final = []
    
    while len(visited) < n:

        temp = stack.popleft()
        node = temp[0]
        distance = temp[1]
        for child in graph[node]:
            if child not in visited:
                visited.add(child)
                stack.append((child,distance+1))
                final.append(distance+1)

    maxi = max(final)

    return final.count(maxi)
