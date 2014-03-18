class ValidPalindrome:
    def isPalindrome(self, s):
        if s is None or len(s) == 0:
            return True

        news = []
        for i in s:
            if '0' <= i <= '9' or 'a' <= i <= 'z':
                news.append(i)
            elif 'A' <= i <= 'Z':
                news.append(chr(ord(i) - ord('A') + ord('a')))

        return news == news[::-1]
