def solution(spell, dic):
    for i in dic:
        stack = set()
        for j in i:
            if j in spell:
                stack.add(j)
            print(stack)
        if len(stack) == len(spell):
            return 1
            
    return 2