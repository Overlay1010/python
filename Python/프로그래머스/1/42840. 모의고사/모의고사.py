def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scores = [0, 0, 0] 
    
    for i, ans in enumerate(answers):
        if ans == a[i % len(a)]:
            scores[0] += 1
        if ans == b[i % len(b)]:
            scores[1] += 1
        if ans == c[i % len(c)]:
            scores[2] += 1
    
    max_score = max(scores)
    answer = [i + 1 for i, score in enumerate(scores) if score == max_score]
    
    return answer