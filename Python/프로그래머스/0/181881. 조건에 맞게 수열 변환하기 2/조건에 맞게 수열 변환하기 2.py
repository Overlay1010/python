def solution(arr):
    answer = 0
    for i in range(len(arr)):
        cnt = 0
        while (arr[i] % 2 ==0 and arr[i] >=50) or (arr[i] % 2 !=0 and arr[i] <= 50):
            if arr[i] % 2 ==0 and arr[i] >=50:
                arr[i] //= 2
            else:
                arr[i] = arr[i] *2 +1
            cnt +=1
        answer = max(answer, cnt)
            
    return answer