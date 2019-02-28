import string
alphabet = list(string.ascii_lowercase)
morse_codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
               "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
alphabet_to_morse = dict(zip(alphabet, morse_codes))

def morse_to_word(word):
    word = list(word)
    morse_string = ''
    for letter in word:
       morse_string += (alphabet_to_morse[letter])
    return morse_string





def morse_code(list_of_words):
    unique_output = []
    for element in list_of_words:
        unique_output.append(morse_to_word(element))

    print(len(set(unique_output)))

morse_code(["gin", "zen", "msg"])