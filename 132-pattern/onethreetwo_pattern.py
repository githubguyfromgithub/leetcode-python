def ranges_overlap(r1, r2):
    if r1[0] > r2[1]:
        return False
    elif r1[1] < r2[0]:
        return False
    else:
        return True

def merge_ranges(r1, r2):
    return (min(r1[0], r2[0]), max(r1[1], r2[1]))

class Solution(object):

    def find132pattern(self, nums):
        ranges = []
        r = (nums[0], nums[0])
        for i in range(1, len(nums)):
            n = nums[i]
            if(n > r[0] and n < r[1]):
                return True
            for old_range in ranges:
                if(n > old_range[0] and n < old_range[1]):
                    return True
            if n > r[1]:
                r = (r[0], n)
            elif n < r[0]:
                if(r[0]< r[1]):
                    merged = False
                    for existing_range_index, existing_range in enumerate(ranges):
                        if ranges_overlap(r, existing_range):
                            ranges[existing_range_index] = merge_ranges(r, existing_range)
                            merged = True
                            break
                    if not merged:
                        ranges.append(r)
                r = (n, n)
        return False
        
        