# https://leetcode.com/problems/valid-palindrome/
from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        def convert(word):
            word = word.lower()
            temp = []
            for i in word:
                if 97 <= ord(i) <= 122 or 48 <= ord(i) <= 57:
                    temp.append(i)

            original = "".join(temp)
            q = deque(temp)
            answer = ""
            while q:
                a = q.pop()
                answer += a
            if answer == original:
                return True
            else:
                return False

        return convert(s)
