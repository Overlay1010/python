def solution(score):
    scores = []
    for s in score:
        scores.append(sum(s) / 2)
    sorted_scores = sorted(scores, reverse=True)
    answer = []
    for avg in scores:
        answer.append(sorted_scores.index(avg) + 1)
    return answer