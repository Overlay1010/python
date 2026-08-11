def solution(numbers):
    answer = ""
    b = ""
    a = {"zero":0,
         "one" :1, 
         "two" : 2, 
         "three" : 3, 
         "four" : 4, 
         "five" : 5, 
         "six" : 6, 
         "seven" : 7, 
         "eight" : 8, 
         "nine" : 9}
    for i in numbers:
        b+=i
        if b in a:
            answer+=str(a[b])
            b=""
    
    return int(answer)