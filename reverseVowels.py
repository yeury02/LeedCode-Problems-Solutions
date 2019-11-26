class Solution:
    def reverseVowels(self, s):
        start = 0
        end = len(s) - 1
        while (start < end):
                if s[start] in "aeiou":
                    if s[end] in "aeiou":
                        self.swap(s,start,end)
                        start += 1
                        end -= 1
                    if s[end] not in "aeiou":
                        end -= 1
                else:
                    start += 1
        return s
    def swap(self, s, start, end):
        tmp = s[start]
        s[start] = s[end]
        s[end] = tmp

s = "hello"
object = Solution()
print(object.reverseVowels(s))