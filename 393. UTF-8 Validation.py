class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """

        index, size = 0, len(data)
        head_mask = 0b10000000

        while index < size:
            head = data[index]
            index += 1

            if head >> 7:      # Check if head staring with 1
                head <<= 1       # Drop the first
                count = 0
                while head & head_mask:     # Check how many following bytes followed head
                    count += 1
                    head <<= 1
                if count < 1 or count > size:   # Check if byte count is available
                    return False

                # Count the following n elements head with '0b10'.
                for _ in range(count):
                    if data[index] >> 6 == 0b10:
                        index += 1
                        count -= 1

                if count:
                    return False
        else:
            return True
