class PalindromeNumber:
    def isPalindrome(self, x):
        if x<0:
            return False
        divider = 1
        while x/divider >= 10:
            divider *= 10

        while x != 0:
            l = x/divider
            r = x%10
            if l != r:
                return False

            x = (x % divider)/10
            divider /= 100

        return True


mySolution = PalindromeNumber()
print (-1, mySolution.isPalindrome(-1))
print (1, mySolution.isPalindrome(1))
print (100, mySolution.isPalindrome(100))
print (1001, mySolution.isPalindrome(1001))
print (101, mySolution.isPalindrome(101))
