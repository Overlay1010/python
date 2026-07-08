# 시간복잡도 검색해보다 카운트방법이 있단걸 알게됨...... 

def solution(X, Y):
    answer = ''
    x = [0] * 10  # 0~9까지 숫자 갯수 넣을 요소
    y = [0] * 10
    for n in X:
        x[int(n)]+=1 # 숫자 등장할때마다 1씩 올리기
    for n in Y:
        y[int(n)]+=1
        
    for i in range(9,-1,-1): # 큰값 으로 바꾸기 위해 9부터 거꾸로....복잡도 shit
        num_count = min(x[i],y[i]) # 공통해서 나오는 수
        answer += str(i)*num_count 
    if len(answer) == 0: # 공통되는 값없을때
        return '-1'
    if answer[0] == '0': #모든 값이 0일때
        return '0'
    return answer