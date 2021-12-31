def solution(N):
    answer = 0

    binary_num = bin(N)[2:]

    binary_num = binary_num.strip('0')

    binary_num = binary_num.split('1')

    for gap in binary_num:

        answer = max(answer, len(gap))

    return answer
