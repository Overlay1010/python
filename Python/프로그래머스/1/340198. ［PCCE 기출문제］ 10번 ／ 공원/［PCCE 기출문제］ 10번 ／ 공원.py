def solution(mats, park):
    mats.sort(reverse=True)
    rows = len(park)
    cols = len(park[0])
    for size in mats:
        for i in range(rows-size+1):
            for j in range(cols-size+1):
                possible = True
                
                for x in range(i,i+size):
                    for y in range(j,j+size):
                        if park[int(x)][int(y)] != '-1':
                            possible = False
                            break
                
                    if not possible:
                        break
                
                if possible:
                    return size
    return -1
            