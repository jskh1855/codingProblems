def solution(A):
    
    is_distinct = defaultdict(int)
    answer = 0

    for num in A:

        if is_distinct[num] == 0 and is_distinct[-num] == 0:

            answer += 1
            is_distinct[num] = 1
            is_distinct[-num] = 1

    return answer
