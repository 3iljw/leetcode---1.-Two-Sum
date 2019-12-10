class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = {}
        for index, value in enumerate(nums) :
            if target - value not in dict_ :
                dict_[value] = index
            else :
                return [dict_[target-value],index]
