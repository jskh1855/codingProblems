#두 배열의 dot product를 찾는 알고리즘

def solution(a, b):
    
    return sum([x*y for x,y in zip(a,b)])
