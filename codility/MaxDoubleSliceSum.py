from collections import defaultdict

def solution(A):
    
    block_sum = defaultdict(int)

    answer = 0
    cur_max = 0

    for i in range(1,len(A)-2):

        if cur_max + A[i] > 0:

            cur_max += A[i]
            block_sum[i+1] = cur_max
            answer = max(answer, cur_max)

        else:

            cur_max = 0

    cur_max = 0

    for j in range(len(A)-2,1,-1):

        if cur_max + A[j] > 0:

            cur_max += A[j]
            answer = max(answer, cur_max+block_sum[j-1])

        else:
            cur_max = 0
            answer = max(answer, block_sum[j-1])

    return answer
