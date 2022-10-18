def solution(A):
    
    A.sort()
    answer = 0

    for i in range(len(A)-2):

        if A[i]+A[i+1] > A[i+2] and A[i+1]+A[i+2] > A[i] and A[i]+A[i+2] > A[i+1]:

            answer = 1
            break

    return answer
