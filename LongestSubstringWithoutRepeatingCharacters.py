class LongestSubstringWithoutRepeatingCharacters:
    def lengthOfLongestSubstring(self, s):
        if (s is None) or (len(s) == 0):
            return 0

        flag = [False] * 256

        i = 0
        j = 0
        maxLength = 0
        length = len(s)

        for i in range(0, length):
            idx = ord(s[i])
            if flag[idx] == True:
                maxLength = max(maxLength, i-j)
                for k in range(j, i):
                    if s[k] == s[i]:
                        j = k+1
                        break
                    flag[ord(s[k])] = False
            else:
                flag[idx] = True

        maxLength = max(maxLength, len(s) - j)

        return maxLength


