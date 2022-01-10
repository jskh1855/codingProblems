from collections import defaultdict

def solution(A):
    
    counter = defaultdict(int)

    for num in A:

        counter[num] += 1

    answer = 1

    while True:

        if counter[answer] < 1:

            break

        answer += 1

    return answer
