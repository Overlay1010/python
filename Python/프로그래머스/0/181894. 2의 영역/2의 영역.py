def solution(arr):
    answer = []
    a= []
    for i in range(len(arr)):
        if arr[i] == 2:
            a.append(i)
    if len(a)>=1:
        answer = arr[a[0]:a[-1]+1]
    else:
        return [-1]
    return answer