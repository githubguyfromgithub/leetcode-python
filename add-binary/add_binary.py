class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        aAsNumbers = [ord(c) - ord('0') for c in a[::-1]]
        bAsNumbers = [ord(c) - ord('0') for c in b[::-1]]

        c = 0
        result = []
        for i in range(max(len(aAsNumbers), len(bAsNumbers))):
            thisValue = c
            if(i < len(aAsNumbers)):
                thisValue += aAsNumbers[i]
            if(i < len(bAsNumbers)):
                thisValue += bAsNumbers[i]
            result.append(thisValue%2)
            c = thisValue // 2
        if c:
            result.append(1)
        return "".join([str(n) for n in result[::-1]])
