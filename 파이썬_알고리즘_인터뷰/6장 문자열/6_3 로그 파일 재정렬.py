class Solution:
    def wordMaker(l, digit, letter):
        for i in range(len(l)):
            if l[i] == " ":
                idx = i
                break
        identifier = (l[:i])
        message = (l[i:])

        if 48 <= ord(message[1]) <= 57:
            digit.append([identifier, message])
        else:
            letter.append([identifier, message])

    def arrToString(arr):
        print(arr)
        result = "".join(arr)
        return result

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit = []
        letter = []
        answer = []
        for i in logs:
            Solution.wordMaker(i, digit, letter)

        letter.sort(key=lambda x: (x[1], x[0]))
        for i in letter:
            answer.append(Solution.arrToString(i))
        for i in digit:
            answer.append(Solution.arrToString(i))
        return answer
