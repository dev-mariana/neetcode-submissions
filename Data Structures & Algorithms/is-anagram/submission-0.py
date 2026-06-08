class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_s = {}

        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1

        freq_t = {}

        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1

        return freq_s == freq_t


# return true if the two passed strings are anagram of each other
# an anagram is a string that contains the exact same characters
# as another string, but the order can be different.

# 1. check is they have the same length
# if not, return false
# 2. count the frequency of each character in s string
# create a map/dicionary for s
# 3. count the frequency of each character in t string
# create a map/dicionary for t
# 4. compare the two frequency maps
# if they're identical, return true, if not return false
