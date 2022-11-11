def solution(A, B):
    
    if len(A) < 2:

        return len(A)

    answer = 1
    i = 0
    j = 1

    while j < len(B):

        if B[i] < A[j]:

            answer += 1
            i = j
            j += 1

        else:
            j += 1

    return answer
