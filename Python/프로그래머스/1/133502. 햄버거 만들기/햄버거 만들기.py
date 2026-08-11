def solution(ingredient):
    answer = 0  
    a =[]
    pattern = [1,2,3,1] # 빵 야채 고기 빵
    for i in ingredient:
        a.append(i)
        if len(a) >= 3 and a[-4:] == pattern:
            # a의 길이가 패턴길이랑 같거나 길때 a의 마지막 4요소가 기본 순서와 같으면 answer+=1
            answer+=1
            del(a[-4:]) # 같으면 지움
    return answer
