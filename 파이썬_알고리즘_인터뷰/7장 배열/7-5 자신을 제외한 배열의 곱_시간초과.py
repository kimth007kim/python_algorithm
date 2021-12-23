# https://leetcode.com/problems/product-of-array-except-self/submissions/

class Solution:
    def multiply(arr):
        total = 1
        for i in arr:
            total *= i
        return total

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        for k, v in enumerate(nums):
            tmp = nums[:]
            del tmp[k]
            answer.append(Solution.multiply(tmp))
        return answer