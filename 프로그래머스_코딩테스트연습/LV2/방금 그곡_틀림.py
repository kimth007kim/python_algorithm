def calcTime(time):
    hr, mi = time.split(":")
    total = int(hr) * 60 + int(mi)
    return total


def word(song, minus, m):
    music = song
    print(song, len(song), minus)
    while len(music) < minus:
        music += song
    if len(music) > minus:
        music = music[:minus]

    print(music, "--------")

    if m[-1] == "#":
        print("##")

    for i in range(0, len(music) - len(m), 1):
        print(music[i:i + len(m)])
        if music[i:i + len(m)] == m:
            return True
    return False

    # for i in range(0,len(music)-len(m),1):
    #     if music[i:i+len(m)] == m:
    #         if m[-1]!="#":
    #             if i+len(m)<len(music) and music[i+len(m)]=="#":
    #                 return False
    #             else:
    #                 return True
    #         else:
    #             return True


def solution(m, musicinfos):
    tmp = []
    answer = ''
    # print("기억한 멜로디를 담은 문자열", m)
    # print("방송된 곡의 정보를 담고 있는 배열 ",musicinfos)
    for i in range(len(musicinfos)):
        s, e, title, song = musicinfos[i].split(",")
        start = calcTime(s)
        end = calcTime(e)
        minus = end - start
        LEN = len(song)
        if word(song, minus, m):
            tmp.append((i, title))

    # tmp.append((2,"THEKING"))

    if len(tmp) == 0:
        return None
    else:
        a = sorted(tmp, key=lambda x: (len(x[1]), x[0]))
        print(a)