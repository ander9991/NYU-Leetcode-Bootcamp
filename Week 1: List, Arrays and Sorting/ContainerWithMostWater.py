class Solution:
    def maxArea(self, height: List[int]) -> int:
        prod = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                int1 = height[i]
                int2 = height[j]
                h = min(int1, int2)
                x = j - i

                if (h * x > prod):
                    prod = h * x
        return prod
        # TODO: Time Limit Exceeded


# Another solution:
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxx = 0 
        i = 0
        j = len(height)-1
        while i < j:
            width = abs(i-j)
            area = width * min(height[i],height[j])
            maxx = max(area,maxx)
            if height[i] > height[j]:
                j -=1
            else:
                i +=1
        return maxx 
