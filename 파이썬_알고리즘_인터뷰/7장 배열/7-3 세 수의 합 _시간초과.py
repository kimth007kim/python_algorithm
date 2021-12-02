class Solution:
    def copier(arr):
        tmp = []
        for i in arr:
            tmp.append(i)
        return tmp

    def add_numbers(box_arr):
        SUM = 0
        for i in box_arr:
            SUM += i
        if SUM == 0:
            return True
        else:
            return False

    def recur(cnt, nums, idx_arr, box_arr):
        if cnt == 3:
            if Solution.add_numbers(box_arr) == True:
                box_arr.sort()
                if box_arr not in answer:
                    answer.append(box_arr)
            return

        for i in range(len(nums)):
            if i not in idx_arr:
                cp_idx = Solution.copier(idx_arr)
                cp_box = Solution.copier(box_arr)

                cp_idx.append(i)
                cp_box.append(nums[i])

                Solution.recur(cnt + 1, nums, cp_idx, cp_box)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        global answer
        nums.sort()

        answer = []
        for i in range(len(nums)):
            Solution.recur(0, nums, [], [])
        return answer