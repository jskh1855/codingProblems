def solution(A):
    
    init = 1
    answer = 1

    A.sort()

    for num in A:

        if num != init:

            answer = 0
            break

        init += 1

    return answer
