class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        ans = 0
        if x < 0:
            sign = -1
        else:
            sign = 1
            
        x = abs(x)
        
        while (x != 0):
            temp = x % 10
            ans = ans * 10 + temp
            x = x / 10
            
        if ans > 2147483647 or ans <= -2147483648:
            ans = 0
            
        return ans * sign
