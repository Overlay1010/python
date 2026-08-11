def solution(array):
    count = [0]*(max(array)+1)
    for i in array:
        count[i]+=1
        
    max_count = max(count)
    answer = [i for i, c in enumerate(count)if c ==max_count]
    
    return answer[0] if len(answer)==1 else -1