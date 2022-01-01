def solution(A, K):
    
    N = len(A)
    answer = [0]*N
    
    for i in range(N):

        answer[(i+K)%N] = A[i]

    return answer
