def reverser(word):
    reversed_string = ''
    for char in word:
        reversed_string = char + reversed_string
    return reversed_string

class Solution:
    def reverseWords(self, s: str) -> str:
        string_to_array = s.split(' ')
        reversed_sentence = ''
        for word in string_to_array:
            if reversed_sentence == '':
                reversed_sentence = reverser(word)
            else:
                reversed_sentence = reversed_sentence + ' ' + reverser(word)
        return reversed_sentence