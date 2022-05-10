class Solution(object):

    def find132pattern(self, nums):
        mins = nums[:]
        for i in range(1, len(nums)):
            mins[i] = min(nums[i], mins[i-1])
        
        stack = []
        for i in range(len(nums)-1, -1, -1):
            k = nums[i]
            if k == mins[i]:
                continue
            while len(stack) > 0 and stack[-1] <= mins[i]:
                stack.pop()
            if len(stack) > 0 and stack[-1] < k:
                return True
            if len(stack) == 0 or k < stack[-1]:
                stack.append(k)
        return False
                

 