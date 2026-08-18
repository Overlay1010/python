def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True)
    answer = [sorted_emergency.index(x) + 1 for x in emergency]
    return answer