def solution(arr, queries):
    answer = []
    for i in queries:
        answer = arr
        for n in range(i[0],i[1]+1):
            if n % i[2] == 0:
                answer[n]+=1

    return answer