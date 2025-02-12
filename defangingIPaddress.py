#Given a valid (IPv4) IP address, return a defanged version of that IP address.

#A defanged IP address replaces every period "." with "[.]".

#For Instance- Input: address = "1.1.1.1"   address = "255.100.50.0"
              #Output: "1[.]1[.]1[.]1"     "255[.]100[.]50[.]0"

class Solution:
    def defangIPaddr(self, address):

        result = []
        for i in range(len(address)):

            if address[i] == '.':
                result.append('[.]')
                continue
            result.append(address[i])
            # joins puts together everything in a list as a string
        return "".join(result)


address = "1.1.1.1"
object = Solution()
#result should be "1[.]1[.]1[.]1
print(object.defangIPaddr(address))
