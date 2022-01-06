def solution(A):
    
    total = sum(A)
    cur = 0
    min_diff = 100000*1000

    for i in range(len(A)-1):

        cur += A[i]
        gap = total - cur
        min_diff = min(min_diff, abs(gap-cur))

    return min_diff
