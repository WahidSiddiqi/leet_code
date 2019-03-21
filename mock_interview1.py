def longest_palin(list_of_palindromes):
    longest_palindrome = list_of_palindromes[0]
    for each_palindrome in list_of_palindromes:
        if len(each_palindrome) > len(longest_palindrome):
            longest_palindrome = each_palindrome
    return longest_palindrome

class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindromes = []
        for i in range(len(s)):
            for j in range(len(s)+1):
                if ''.join(s[i:j]) == (''.join(s[i:j]))[::-1] and len(s[i:j]) >= 2:
                    palindromes.append(''.join(s[i:j]))
        print(longest_palin(palindromes))

    longestPalindrome('babad')