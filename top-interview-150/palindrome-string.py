def is_palindrome(s):
    reverse_s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]

print(is_palindrome("radar"))         # Output: True
print(is_palindrome("python"))        # Output: False
print(is_palindrome("A man, a plan"))  # Output: True
