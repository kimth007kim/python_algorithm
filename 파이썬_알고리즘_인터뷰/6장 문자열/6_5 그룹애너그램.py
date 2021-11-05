class Solution:
    def wordMaker(word, gram):
        tmp = list(word)
        tmp.sort()
        print(tmp)
        id = "".join(tmp)
        if id not in gram:
            gram[id] = [word]
        else:
            gram[id].append(word)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gram = {}
        for word in strs:
            Solution.wordMaker(word, gram)
        answer = []
        for i in gram:
            answer.append(gram[i])
        return answer