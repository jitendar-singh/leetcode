# Write a Python function to determine if a given string is a palindrome

def is_palindrome(mystr):
    mystr = mystr.lower().replace(" ","")
    return mystr == mystr[::-1]

print(is_palindrome("racecar"))         # Output: True
print(is_palindrome("level"))           # Output: True
print(is_palindrome("Python"))          # Output: False
print(is_palindrome("A man a plan"))     # Output: True
print(is_palindrome("hello world"))      # Output: False