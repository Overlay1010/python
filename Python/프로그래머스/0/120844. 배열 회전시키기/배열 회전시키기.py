def solution(numbers, direction):
    answer = []
    for i in numbers:
        if direction == 'right':
            answer = numbers[-1:]+numbers[:-1]
        else:
            answer = numbers[1:]+numbers[:1]
    return answer