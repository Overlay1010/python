def solution(arr):
    row = len(arr)
    col = len(arr[0])
    size = max(row, col)
    
    answer = []
    for r in arr:
        new_row = r + [0] * (size - len(r))  
        answer.append(new_row)
    

    while len(answer) < size:
        answer.append([0] * size)
    
    return answer