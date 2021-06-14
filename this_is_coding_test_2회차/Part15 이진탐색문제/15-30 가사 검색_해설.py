from bisect import bisect_left, bisect_right

words=["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries=["fro??", "????o", "fr???", "fro???", "pro?"]

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    print(right_index)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]


def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    print(array[5])
    print(queries[0][::-1])

    for q in queries:
        if q[0] != "?":
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))           #ex) fro 라면 froaa~frozz까지 있는지 확인
            print("-----",res)
        else:
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(res)
    return answer


print(solution(words,queries))