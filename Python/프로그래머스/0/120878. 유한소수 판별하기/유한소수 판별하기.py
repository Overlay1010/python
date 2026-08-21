def solution(a, b):
    answer = 0
    a_lst = []
    b_lst = []
    num = []
    for i in range(2,a+1):
        if a % i ==0:
            a_lst.append(i)
    for j in range(2, b+1):
        if b % j ==0:
            b_lst.append(j)
    for x in a_lst:
        for y in b_lst:
            if x == y:
                num.append(x)
    if not num:
        num.append(1)
    n = max(num)
    b = b//n
    while b % 2 == 0:
        b//= 2
    while b % 5 == 0:
        b//= 5
    if b == 1 :
        return 1 
    else:
        return 2    
    # print(max_num)
                