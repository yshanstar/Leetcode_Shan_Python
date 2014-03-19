class ValidParentheses:
    def isValid(self, s):
        stack = []
        pushCharStack = "<{[("
        popCharStack = ">}])"

        for c in s:
            if c in pushCharStack:
                stack.append(c)
            elif c in popCharStack:
                if not len(stack):
                    return False
                else:
                    top = stack.pop()
                    backBracket = pushCharStack[popCharStack.index(c)]
                    if top != backBracket:
                        return False
            else:
                return False

        return not len(stack)
