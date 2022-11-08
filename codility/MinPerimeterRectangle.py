def solution(N):

    answer = 0

    for i in range(1, int(N**(1/2))+1):

        if N%i == 0:

            answer = 2*(N//i+i)

    return answer
