def solution(price, money, count):
    answer = 0
    n = 0
    for i in range(1,count+1):
        n += price*i
        if money < n:
            answer = n - money
        else:
            answer = 0

    return answer