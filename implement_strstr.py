class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)
        needle_list = list(needle)
        haystack_list = list(haystack)
        if needle not in haystack:
            return -1
        elif needle in haystack:
            for char in range(len(haystack) - len(needle) + 1):
                if haystack_list[char:len_needle] == needle_list:
                    return char
                elif needle == '':
                    return null
                len_needle += 1