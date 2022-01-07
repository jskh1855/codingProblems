def solution(X, A):
    
    position_to_leaf = {}
    
    for i in range(len(A)):
        
        if position_to_leaf.get(A[i], -1) == -1:
            position_to_leaf[A[i]] = i

    cur_pos = 1
    answer = -1

    while cur_pos <= X:

        if position_to_leaf.get(cur_pos,-1) == -1:
            answer = -1
            break
        
        answer = max(answer, position_to_leaf[cur_pos])
        cur_pos += 1

    return answer
