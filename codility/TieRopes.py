def solution(K, A):
    
    answer = 0
    i = 0
    length = 0

    while i < len(A):

        length += A[i]

        if length >= K:

            answer += 1
            length = 0

        i += 1

    return answer
