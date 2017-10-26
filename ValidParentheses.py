class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False
        
        paren_list = []
        paren_dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in paren_dict.values():
                paren_list.append(char)
            elif char in paren_dict.keys():
                if len(paren_list) == 0 or paren_dict[char] != paren_list.pop():
                    return False
            else:
                return False
        return len(paren_list) == 0
