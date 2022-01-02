def solution(A):
    answer = 0
    num_dict = defaultdict(int)

    for num in A:

        num_dict[num] += 1

    for key, value in num_dict.items():

        if value%2 != 0:

            answer = key
            break

    return answer
