class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """

        size = len(data)

        head_mask = 0b10000000

        while data:
            head = data.pop(0)
            size -= 1

            if head >> 7:      # Check if head staring with 1
                head <<= 1       # Drop the first
                n = 0
                while head & head_mask:     # Check how many following bytes followed head
                    n += 1
                    head <<= 1
                if n < 1 or n > size:   # Check if byte count is available
                    return False

                count = 0               # Count the following n elements head with '0b10'.
                for i in range(n):
                    if data[i] >> 6 == 0b10:
                        count += 1

                if count != n:
                    return False
                else:
                    data = data[n:]     # Step forward
        else:
            return True
            
