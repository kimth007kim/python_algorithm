# https://leetcode.com/problems/product-of-array-except-self/submissions/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        for i in range(len(nums)):
            out.append(p)
            p = p * nums[i]
        p = 1
        print()
        for i in range(len(nums) - 1, -1, -1):
            print("out[{}]={} , p= {}".format(i, out[i], p))
            out[i] = out[i] * p
            print(out)
            p = p * nums[i]
            print(p)
        return out