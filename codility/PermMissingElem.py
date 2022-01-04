def solution(A):
    
    counter = {num:1 for num in A}
    answer = 1

    for i in range(1,len(A)+2):

        if counter.get(i,0) == 0:
            answer = i
            break

    return answer
