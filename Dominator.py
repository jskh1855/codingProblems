def solution(A):

    mapper = defaultdict(int)
    answer = -1

    half = len(A)//2

    for i in range(len(A)):

        mapper[A[i]] += 1
        if mapper[A[i]] > half:

            answer = i
            break

    return answer
