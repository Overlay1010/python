def solution(nums):
    pokemon_types = len(set(nums))  # 폰켓몬 종류 수
    selectable_count = len(nums) // 2  # 선택 가능한 수

    return min(pokemon_types, selectable_count)