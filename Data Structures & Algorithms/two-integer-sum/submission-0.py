class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = dict() #{key : value}
        #dict is all about efficiently returning a value based on a key

        for i in range(len(nums)):
            num = nums[i] # num = 3

            
            complement = target - num # 4
            if complement in complements:
                return [complements[complement], i]

            else:
                complements[num] = i #3:0

            