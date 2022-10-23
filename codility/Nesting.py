def solution(S): 

    answer = 1
    stack = []
    s_list = list(S)

    while s_list:

        cur_char = s_list.pop()

        if cur_char == ')':

            stack.append(cur_char)
            continue

        else:
            if not stack:

                answer = 0
                break

            if stack[-1] == ')':

                stack.pop()

            else:

                answer = 0
                break

    if stack:

        answer = 0

    return answer
