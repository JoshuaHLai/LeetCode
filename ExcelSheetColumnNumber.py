class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.upper()
        answer = 0
        for letter in s:
            answer = answer * 26 + ord(letter) - 64
        return answer
