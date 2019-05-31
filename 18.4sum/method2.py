class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        nums.sort()
        res = set()
        for i_1, v_1 in enumerate(nums[:-3]):
            for i_2, v_2 in enumerate(nums[i_1 + 1:-2]):
                left = i_1+i_2 + 2
                right = len(nums) - 1
                while left < right:
                    if v_1 + v_2 + nums[left] + nums[right] == target:
                        res.add((v_1, v_2, nums[left], nums[right]))
                        left += 1
                    elif v_1 + v_2 + nums[left] + nums[right] < target:
                        left += 1
                    else:
                        right -= 1
        res = [list(item) for item in res]
        return res
