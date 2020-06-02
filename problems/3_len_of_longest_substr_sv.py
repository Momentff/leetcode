class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        for k in range(len(s)):
            if k == 0:
                temp_str = s[k]
                max = 1
            else:
                if s[k] not in temp_str:
                    temp_str += s[k]
                    if len(temp_str) > max:
                        max = len(temp_str)
                    if k == len(s) - 1:
                        return max
                else:
                    temp_str = temp_str[temp_str.index(s[k])+1:] + s[k]
        return max