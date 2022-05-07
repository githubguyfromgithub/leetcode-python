class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxValues = [None]*len(nums);
        maxValues[0] = nums[0]
        for i in range(1,len(nums)):
            maxValues[i] = max(nums[i], maxValues[i-1])
        max32s = [None]*len(nums)
        for i in range(1, len(nums)):
            is32 = nums[i] < maxValues[i-1]
            if is32:
                max32s[i] = nums[i] if max32s[i-1] == None else max(nums[i], max32s[i-1])
            else:
                max32s[i] = max32s[i-1]
        for i in range(len(nums)-2):
            if nums[i] < max32s[-1]:
                return True
        return False
        
        