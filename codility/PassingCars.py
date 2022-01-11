def solution(A):
    answer = 0
    passing_cars = 0
    maximum = 1000000000

    while len(A):

        car = A.pop()
        if car == 0:
            answer += passing_cars
            continue
        
        passing_cars += 1

    if answer > maximum:
        return -1
    
    return answer
