def solution(order):
    answer = 0
    ame =["iceamericano",
          "americanoice",
          "hotamericano", 
          "americanohot",
          'americano',
          'anything']
    latte = ['cafelatte',
             "icecafelatte", 
             "cafelatteice",
             "hotcafelatte", 
             "cafelattehot"]
    for o in order:
        if o in ame:
            answer+=4500
        else:
            answer+=5000
    return answer