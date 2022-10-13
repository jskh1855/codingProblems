def solution(S, P, Q):
    
    answer = []
    mapper = {'A':1, 'C':2, 'G':3, 'T':4}

    a_list, c_list, g_list, t_list = [0]*len(S), [0]*len(S), [0]*len(S), [0]*len(S)

    for i in range(len(S)):

        if S[i] == 'A':

            a_list[i] += 1

        if S[i] == 'C':

            c_list[i] += 1

        if S[i] == 'G':

            g_list[i] += 1

        if S[i] == 'T':

            t_list[i] += 1

    for i in range(1,len(S)):

        a_list[i] += a_list[i-1]
        c_list[i] += c_list[i-1] 
        g_list[i] += g_list[i-1] 
        t_list[i] += t_list[i-1]

    for i, j in zip(P, Q):

        if i == j:

            answer.append(mapper[S[i]])
            continue

        if S[i] == 'A' or a_list[j] - a_list[i] > 0:

            answer.append(1)
            continue

        if S[i] == 'C' or c_list[j] - c_list[i] > 0:

            answer.append(2)
            continue

        if S[i] == 'G' or g_list[j] - g_list[i] > 0:

            answer.append(3)
            continue

        if S[i] == 'T' or t_list[j] - t_list[i] > 0:

            answer.append(4)
            continue

    return answer
