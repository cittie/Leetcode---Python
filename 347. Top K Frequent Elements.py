class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequent_dict = {}

        for _ in range(len(nums)):
            if nums[_] in frequent_dict:
                frequent_dict[nums[_]] += 1
            else:
                frequent_dict[nums[_]] = 1
        
        freq_nums = sorted(frequent_dict, key = frequent_dict.get, reverse = True)

        return freq_nums[:k]