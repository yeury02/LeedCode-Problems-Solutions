

#S and J will consist of letters and have length at most 50.
#The characters in J are distinct.
class Solution:
    def numJewelsInStones(self, J, S):
        count = 0
        for ch in S:
            if ch in J:
                count+=1
        return count

J = "aA"
S = "aAAbbbb"
#output should be 3
object = Solution()
print(object.numJewelsInStones(J,S))