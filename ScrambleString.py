class ScrambleString:
    # @return a boolean
    def isScramble(self, s1, s2):
        if s1 is None and s2 is None:
            return True
        elif s1 is None or s2 is None:
            return False
        elif s1 == s2:
            return True

        if len(s1) != len(s2):
            return False

        strVal1 = 0
        strVal2 = 0

        for i in range(0, len(s1)):
            strVal1 = strVal1 + ord(s1[i])
            strVal2 = strVal2 + ord(s2[i])

        if strVal1 != strVal2:
            return False

        for i in range(1, len(s1)):
            if self.isScramble(s1[0 : i], s2[0 : i]) and self.isScramble(s1[i:], s2[i:]):
                return True

            if self.isScramble(s1[0 : i], s2[-i:]) and self.isScramble(s1[i:], s2[ : -i]):
                return True

        return False


x = ScrambleString()
print (x.isScramble("abb", "bba"))