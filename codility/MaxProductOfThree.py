def solution(A):
    
    A.sort()

    answer= max(A[0]*A[1]*A[-1], A[-1]*A[-2]*A[-3])

    return answer
