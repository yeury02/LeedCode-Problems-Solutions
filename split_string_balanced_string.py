#Balanced strings are those who have equal quantity of 'L' and 'R' characters.

#Given a balanced string s split it in the maximum amount of balanced strings.

#Return the maximum amount of splitted balanced strings.

class Solution:
    def balancedStringSplit(self, s):
        lcount = 0
        rcount = 0
        count = 0
        for i in range(len(s)):
            if s[i] == "R":
                rcount += 1
            if s[i] == "L":
                lcount += 1
            if lcount == rcount:
                count += 1
        return count

s = "RLRRLLRLRL"
object = Solution()
print(object.balancedStringSplit(s))