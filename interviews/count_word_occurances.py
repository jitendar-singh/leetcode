# Write a Python program to count the number of occurrences of each word in a given text.

def count_words(text):
    cleaned_text = text.lower().replace(".", "").replace(",", "")
    text = cleaned_text.split()
    count = {}
    for word in text:
        if word in count.keys():
            count[word]+=1
        else:
            count[word]=1
    return count

text = "This is a sample text. It contains words, punctuation, and words again."
count = count_words(text)
print(count)