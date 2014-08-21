__author__ = 'shye'
class RestoreIPAddresses:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        RestoreIPAddresses.res = []
        self.helper('', s, 0)
        return RestoreIPAddresses.res

    def helper(self, curIP, s, idx):
        if idx == 3:
            if len(s) > 0 :
                if str(int(s)) == s and int(s) <= 255:
                    RestoreIPAddresses.res.append(curIP+s)
            return
        length = len(s)
        for i in range(1,4):
            if length >= i and str(int(s[0:i])) == s[0:i] and int(s[0:i]) <= 255:
                self.helper(curIP+s[0:i]+'.', s[i:], idx+1)
        return