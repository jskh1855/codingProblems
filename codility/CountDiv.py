def solution(A, B, K):
    
    answer = 0
    init = B+1

    for i in range(A,B+1):

        if i%K == 0:

            init = i
            answer = 1
            break

    if init < B:

        answer += B//K - init//K

    return answer
