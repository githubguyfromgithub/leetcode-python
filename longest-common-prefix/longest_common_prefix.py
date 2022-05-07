class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        for i,c in enumerate(strs[0]):
            for s in strs[1:]:
                if len(s) <= i or s[i] != c:
                    return strs[0][:i]
        return strs[0]
        