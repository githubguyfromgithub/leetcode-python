class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        l = 0
        r = len(nums) - 1
        count = 0
        while (r > l):
            s = nums[r] + nums[l]
            if s > k:
                r -= 1
            elif s < k:
                l += 1
            else:
                count += 1
                l += 1
                r -= 1
        return count
