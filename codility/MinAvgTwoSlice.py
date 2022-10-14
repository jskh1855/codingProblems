def solution(A):

    mini = 20000
    answer = 0
    
    for i in range(len(A)):

        if i + 1 < len(A):

            if mini > (A[i]+A[i+1])/2:

                mini = (A[i]+A[i+1])/2
                answer = i

            if i + 2 < len(A):

               if mini > (A[i]+A[i+1]+A[i+2])/3:

                mini = (A[i]+A[i+1]+A[i+2])/3
                answer = i                   

    return answer
