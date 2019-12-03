class Solution:
    def numJewelsInStones(self, J, S):
        count = 0
        for ch in S:
            if ch in J:
                count+=1
        return count

J = "aA"
S = "aAAbbbb"
object = Solution()
print(object.numJewelsInStones(J,S))