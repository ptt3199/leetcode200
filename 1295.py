class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for num in nums:
            num_str = str(num)
            if len(num_str) % 2 == 0:
                count += 1
        return count
        