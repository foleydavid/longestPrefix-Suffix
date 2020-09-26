class Solution(object):
    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        s_len = len(s)
        index = 1       # MUST ALLOW FOR CHAR ON EITHER SIDE OF PREFIX/ SUFFIX
        
        # START AT LONGEST POSSIBLE PREFIX, SUFFIX AND WORK DOWN IN LENGTH
        # BREAK OUT ONCE FOUND
        while index < len(s):
            if s[:s_len - index] == s[index:]:
                ans = s[index:]
                break
            else:
                index += 1
            
        return ans
