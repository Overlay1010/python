def solution(sizes):
    max_width = 0
    max_height = 0

    for width, height in sizes:
        # 긴 쪽을 가로, 짧은 쪽을 세로로 배치
        max_width = max(max_width, max(width, height))
        max_height = max(max_height, min(width, height))

    return max_width * max_height