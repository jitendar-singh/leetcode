def sentense_reversal(s):
    words, spaces, length, i = [], ' ', len(s), 0

    while i < length:
        if s[i] not in spaces:
            word_start = i
            while i < length and s[i] not in spaces:
                i+=1
            words.append(s[word_start:i])
        i+=1
    return " ".join(reversed(words))

sentence = 'This is the best'
#output = 'best the is This'
output = sentense_reversal(sentence)
print(output)