def solution(sides):
    n = 0
    cnt = 0
    a = sides[0]
    b = sides[1]
    if a <= b:
        for i in range(b+1):
            if i+a > b:
                cnt+=1
        for i in range(b+1,a+b):
            cnt+=1
    elif a >= b:
        for i in range(a+1):
             if i+b > a:
                cnt+=1
        for i in range(a+1,a+b):
            cnt+=1
    
    
    
    return cnt