#Write a function that reverses a string. The input string is given as an array of characters char[].

#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

#You may assume all the characters consist of printable ascii characters.

class Solution:
    def reverseString(self, s):
        start = 0
        end = len(s) - 1
        while (start < end):
            tmp = s[start]
            s[start] = s[end]
            s[end] = tmp
            start += 1
            end -= 1
        return s

s = ["h","e","l","l","o"]
object = Solution()
print(object.reverseString(s))