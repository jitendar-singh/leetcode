# Problem: Word Lengths
# Write a Python program that takes a list of words as input and returns a new list containing the lengths of each word.
# Example:
# Input: ["apple", "banana", "cherry"]
# Output: [5, 6, 6]

def wordlenght(words):
    return [len(word) for word in words]

if __name__ == "__main__":
    words = ["apple", "banana", "cherry", "Jitendar Singh"]
    print(wordlenght(words))
