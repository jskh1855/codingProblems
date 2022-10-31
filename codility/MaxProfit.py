def solution(A):
    
    answer = 0

    if len(A) < 2:

        return answer

    init = A[0]

    for i in range(1, len(A)):

        answer = max(answer, A[i] - init)
        init = min(init, A[i])

    return max(answer, A[-1] - init)
