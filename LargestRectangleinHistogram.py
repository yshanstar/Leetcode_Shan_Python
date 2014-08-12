__author__ = 'shye'
class LargestRectangleinHistogram:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        stack = []
        i = 0
        maxArea = 0
        while i < len(height):
            if stack == [] or height[i] > height[stack[len(stack)-1]]:
                stack.append(i)
            else:
                cur = stack.pop()
                width = i if stack == [] else i - stack[len(stack)-1] - 1
                maxArea = max(maxArea, width * height[cur])
                i -= 1
            i += 1
        while stack != []:
            cur = stack.pop()
            width = i if  stack == [] else len(height)-stack[len(stack)-1]-1
            maxArea = max(maxArea, width * height[cur])
        return maxArea

myTest = LargestRectangleinHistogram()
print(myTest.largestRectangleArea([1,2,3,4,1]))