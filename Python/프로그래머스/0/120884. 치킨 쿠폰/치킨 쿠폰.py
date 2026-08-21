def solution(chicken):
    answer = 0
    cnt = 0
    while chicken:
        chicken -=1
        cnt +=1
        if cnt%10 ==0:
            answer+=1
            chicken+=1
    return answer