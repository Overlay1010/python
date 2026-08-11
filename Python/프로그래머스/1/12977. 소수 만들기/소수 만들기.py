def solution(nums):
    answer = 0
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                sum_num = nums[i]+nums[j]+nums[k]
                if sum_num < 2:
                    continue
                isnum = True
                for d in range(2,int(sum_num**0.5)+1):
                    if sum_num % d == 0:
                        isnum = False
                        break
                if isnum:
                    answer+=1

                            
    return answer