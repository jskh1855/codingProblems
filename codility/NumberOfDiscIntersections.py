def solution(A):
    
    answer = 0
    edges = []
    for i in range(len(A)):

        edges.append((i-A[i],1))
        edges.append((i+A[i],-1))

    edges.sort(key = lambda x:(x[0],-x[1]))
    
    cur_circles = 1

    for i in range(1,len(edges)):

        if edges[i][1] == 1:

            answer += cur_circles*1
            cur_circles += 1

        if edges[i][1] == -1:

            cur_circles -= 1

    return answer if answer <= 10000000 else -1
