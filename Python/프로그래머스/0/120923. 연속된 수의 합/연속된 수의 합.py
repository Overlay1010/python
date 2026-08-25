def solution(num, total):
    answer = []
    a = []
    for i in range(-1000,1000):
        a.append(i)
    
    for n in range(len(a)-num+1):
        current_sum = sum(a[n:n+num])
        if current_sum == total:
            answer=a[n:n+num]
    return answer