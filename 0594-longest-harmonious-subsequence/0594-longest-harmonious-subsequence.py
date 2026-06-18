from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        arr_counter = Counter(nums)
        max_val = 0

        for key in arr_counter:
            if key + 1 in arr_counter:
                max_val = max(
                    max_val,
                    arr_counter[key] + arr_counter[key + 1]
                )

        return max_val


        # nums.sort()

        # left = 0
        # max_val = 0

        # for right in range(len(nums)):
        #     while nums[right] - nums[left] > 1:
        #         left += 1

        #     if nums[right] - nums[left] == 1:
        #         max_val = max(max_val, right - left + 1)

        # return max_val