class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        n = len(nums)
        num_dict = collections.defaultdict(int)     # key: num, value: index
        
        for i in range(n):
            if nums[i] in num_dict:
                return [i, num_dict[nums[i]]]
            else:
                num_dict[target - nums[i]] = i
