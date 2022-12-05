def solution(A):
    
    counts = 0
    peaks = []

    for i in range(1, len(A)-1):

        if A[i] > A[i-1] and A[i] > A[i+1]:

            counts += 1
            peaks.append(i)

    if len(peaks) == 0:

        return 0

    block = len(A) // len(peaks)

    answer = 1

    while block < len(A):

        if len(A) % block != 0:

            block += 1
            continue
        
        end_of_block = block-1
        index = 0
        has_peak = False

        while index < len(peaks):

            if peaks[index] <= end_of_block:

                has_peak = True
                index += 1

            else:
                if has_peak:
                    end_of_block += block
                    has_peak = False

                else:
                    break

        else:

            answer = len(A) // block
            break

    return answer
