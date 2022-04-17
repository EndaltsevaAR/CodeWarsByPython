"""Description
Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed
characters of S with all the even-indexed characters of S, this process should be repeated N times.

Examples:

encrypt("012345", 1)  =>  "135024"
encrypt("012345", 2)  =>  "135024"  ->  "304152"
encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

encrypt("01234", 1)  =>  "13024"
encrypt("01234", 2)  =>  "13024"  ->  "32104"
encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
Together with the encryption function, you should also implement a decryption function which reverses the process.

If the string S is an empty value or the integer N is not positive, return the first argument without changes."""


def decrypt(text, n):
    for circle in range(n):
        result_word = ''
        first_part = text[int(len(text) / 2)::]
        second_part = text[0:int(len(text) / 2):]
        for letter in range(max(len(first_part), len(second_part))):
            if letter < len(first_part):
                result_word += first_part[letter]
            if letter < len(second_part):
                result_word += second_part[letter]
        text = result_word
    return text


def encrypt(encrypted_text, n):
    for circle in range(n):
        encrypted_text = encrypted_text[1::2] + encrypted_text[::2]
    return encrypted_text


encrypt("This is a test!", 1)
