def solution(progresses, speeds):
    answer = []
    deploy_day = 0
    count = 0

    for progress, speed in zip(progresses, speeds):
        # 해당 기능이 완료되기까지 필요한 날짜
        days = (100 - progress + speed - 1) // speed

        if days > deploy_day:
            # 이전 배포 그룹 저장
            if count > 0:
                answer.append(count)

            deploy_day = days
            count = 1
        else:
            # 앞 기능이 배포될 때 함께 배포
            count += 1

    answer.append(count)

    return answer