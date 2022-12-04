def solution(A):
    
    peaks = []
    answer = 0

    for i in range(1,len(A)-1):

        if A[i-1] < A[i] and A[i] > A[i+1]:

            peaks.append(i)

    if len(peaks) < 3:

        return len(peaks)
    
    flags = int((peaks[-1]-peaks[0])**(0.5))+1

    while flags > 2:

        cur_flags = flags-1
        cur_max = 1
        prev = 0

        for i in range(1,len(peaks)):

            if cur_flags == 0:

                break

            if peaks[i]-peaks[prev] >= flags:

                cur_max += 1
                cur_flags -= 1
                prev = i

        if cur_max >= answer:

            answer = cur_max
            flags -= 1

        else:
            break
    
    return answer
