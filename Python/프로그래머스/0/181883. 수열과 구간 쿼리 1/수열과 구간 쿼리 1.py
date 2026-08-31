def solution(arr, queries):
    answer = []
    answer = arr
    for n in range(len(queries)):
        x,y  = queries[n]
        for i in range(len(arr)):
            if x <= i <= y:
                answer[i]+=1
        
    return answer