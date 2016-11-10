class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        bit_array = [0] * (num + 1)
        bit_array[0], bit_array[1] = 0, 1
        power = 1
        
        while 2 ** power <= num:
            start = 2 ** power
            end = 2 ** (power + 1) - 1
            pointer = start
            
            while pointer <= end and pointer <= num:
                bit_array[pointer] = bit_array[pointer - start] + 1
                pointer += 1
            
            power += 1
            
        return bit_array