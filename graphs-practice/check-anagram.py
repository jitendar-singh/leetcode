def check_anagram(str1, str2):
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ','').lower()

    if len(str1) != len(str2):
        return False
    
    char_freq1, char_freq2 = {}, {}

    for char in str1:
        char_freq1[char] = char_freq1.get(char,0) + 1
    
    for char in str2:
        char_freq2[char] = char_freq2.get(char,0) + 1
    
    return char_freq1 == char_freq2
    


string1 = "listen"
string2 = "siilent"
is_anagram = check_anagram(string1, string2)
print(is_anagram)
