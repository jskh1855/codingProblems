def solution(N, A):
    
    answer = [0 for _ in range(N)]

    max_counter = N+1
    cur_maxi = 0
    operated = 0

    for order in A:

        if order == max_counter:
            operated = cur_maxi

        else:
            if answer[order-1] < operated:
                answer[order-1] = operated+1
            
            else:
                answer[order-1] += 1

            cur_maxi = max(cur_maxi, answer[order-1])

    for i in range(N):

        if answer[i] < operated:

            answer[i] = operated

    return answer
