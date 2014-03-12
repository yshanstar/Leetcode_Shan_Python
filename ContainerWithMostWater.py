class ContainerWithMostWater:
    def maxArea(self, height):
        result = 0

        start = 0
        end = len(height) - 1

        while start < end:
            contain = (end - start) * min(height[start], height[end])
            result = max(contain, result)

            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1

        return result

