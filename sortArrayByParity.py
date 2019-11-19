''' Sort Array by Parity:
Given an array A of non-negative integers, return an array consisting of all the even elements of A,
followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

For example --> Input [3,1,2,4]
               output [2,4,3,1] or [2,4,1,3] or [4,2,3,1] or [4,2,1,3]
'''

class Solution:
    def sortArrayByParity(self, A):
        ParityList = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                ParityList.append(A[i])
        for i in range(len(A)):
            if A[i] % 2 != 0:
                ParityList.append(A[i])
        return ParityList

List = [3,1,2,4]
object = Solution()
print(object.sortArrayByParity(List))