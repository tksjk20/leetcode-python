class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4: return []
        nums.sort()
        res = set()
        for i_1,v_1 in enumerate(nums[:-3]):
            if i_1 >= 1 and nums[i_1] == nums[i_1 - 1]:
                continue
            for i_2,v_2 in enumerate(nums[i_1 + 1:-2]):
                if i_2 >= 1 and nums[i_1 +1+i_2] == nums[i_1 + i_2]:
                    continue
                diff = set()
                for x in nums[i_1 + i_2 + 2:]:
                    if x not in diff:
                        diff.add(target - v_1 - v_2 - x)
                    else:
                        res.add((v_1, v_2, target-v_1-v_2-x, x))
        res = [list(item) for item in res]
        return res