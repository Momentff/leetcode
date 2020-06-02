class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = ""
        max = 0 if len(s) == 0 else 1
        for k in s:
            if string:
                if k not in string:
                    string += k
                else:
                    for i in range(len(string)):
                        if string[i] == k:
                            break
                    string = string[i+1:] + k
                if len(string) > max:
                    max = len(string)
            else:
                string = k
        return max