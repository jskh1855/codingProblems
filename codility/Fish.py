def solution(A, B):
    stack = []
    answer = 0

    while A:

        cur_fish = A.pop()
        cur_stream = B.pop()

        if cur_stream == 1:

            if stack:

                while stack:

                    fish = stack.pop()

                    if cur_fish < fish:
                        
                        stack.append(fish)
                        break

                else:

                    answer += 1

            else:
                
                answer += 1

        else:

            stack.append(cur_fish)

    answer += len(stack)

    return answer
