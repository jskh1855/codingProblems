from collections import defaultdict

def solution(A):
    
    mapper = defaultdict(int)
    answer = 0
    ladder = 0
    remain_count = 0

    for i in range(len(A)):

        mapper[A[i]] += 1

        if mapper[A[i]] > len(A)//2:

            ladder = A[i]

    remain_count = mapper[ladder]
    cur_count = 0

    for i in range(len(A)):

        if A[i] == ladder:

            cur_count += 1
            remain_count -= 1

        if cur_count > (i+1) // 2 and (remain_count) > (len(A)-i-1) // 2:

            answer += 1

    return answer
