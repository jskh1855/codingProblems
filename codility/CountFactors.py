def solution(N):
    
    answer = 1

    if N == 1:

        return answer

    answer += 1

    for i in range(2,int(N**(1/2))+1):

        if N%i == 0:

            answer += 2

            if int(N//i) == i:

                answer -= 1

    return answer
