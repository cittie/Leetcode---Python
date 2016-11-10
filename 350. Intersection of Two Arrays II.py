class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_dict = {}
        nums2_dict = {}
        result = []
        
        for i in range(len(nums1)):
            if nums1[i] in nums1_dict:
                nums1_dict[nums1[i]] += 1
            else:
                nums1_dict[nums1[i]] = 1
        
        for j in range(len(nums2)):
            if nums2[j] in nums1_dict:
                if nums2[j] in nums2_dict:
                    if nums2_dict[nums2[j]] < nums1_dict[nums2[j]]:
                        nums2_dict[nums2[j]] += 1
                        result.append(nums2[j])
                else:
                    nums2_dict[nums2[j]] = 1
                    result.append(nums2[j])
        
        return result
        