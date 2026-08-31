def solution(hp):
    answer = 0
    a,b=5,3
    answer = hp//a+ (hp%a)//b + (hp% a) % b
    
    return answer