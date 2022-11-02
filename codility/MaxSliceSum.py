def solution(A):
    
    answer = max(A)

    if answer < 1:

        return answer

    cur = 0

    for i in range(len(A)):

        if A[i] < 0:

            if cur+A[i] > 0:

                cur += A[i]

            else:

                cur = 0

        else:

            cur += A[i]
            answer = max(answer, cur)

    return answer
