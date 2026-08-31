def solution(price):
    answer = 0
    if 300_000 > price >= 100_000 :
        answer = price * 0.95
    elif 500_000 > price >= 300_000 :
        answer = price * 0.90
    elif price >= 500_000 :
        answer = price * 0.80
    else:
        answer = price
    return int(answer)