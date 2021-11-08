class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                print("left= {} right= {}".format(left, right))
            return s[left + 1:right]

        if len(s) < 2 or s == s[::-1]:
            return s
        result = ''
        for i in range(len(s) - 1):
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
        return result