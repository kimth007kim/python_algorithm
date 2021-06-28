def solution(absolutes, signs):
    length= len(signs)
    number=0
    for i in range(length):
        # print(signs[i])
        if signs[i]==True:
            number+=absolutes[i]
        else:
            number-=absolutes[i]
    # answer = 123456789
    return number