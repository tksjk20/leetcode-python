import collections


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        if len(nums) < 4 or 4*nums[0] > target or 4*nums[-1] < target:
            return []
        total_map = collections.defaultdict(list)
        res = set()
        for num1 in range(len(nums)-1):
            for num2 in range(num1+1, len(nums)):
                diff = target - nums[num1] - nums[num2]
                total_map[diff].append([num1, num2])
        for num1 in range(len(nums) - 3):
            for num2 in range(num1+1, len(nums) - 2):
                total = nums[num1] + nums[num2]
                if total in total_map:
                    for pair in total_map[total]:
                        if pair[0] > num2:
                            res.add((nums[num1], nums[num2],
                                     nums[pair[0]], nums[pair[1]]))
        return [list(item) for item in res]
