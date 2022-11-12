def solution(H):
    
    answer = 0
    stack = []

    while H:

        block = H.pop()

        if stack:

            if block == stack[-1]:

                continue
              
            elif block < stack[-1]:

                while stack:

                    if stack[-1] > block:
  
                        answer += 1
                        stack.pop()

                    elif stack[-1] == block:

                        stack.pop()

                    else:

                        break

                stack.append(block)           

            else:

                stack.append(block)

        else:
            stack.append(block)

    return answer + len(stack)
