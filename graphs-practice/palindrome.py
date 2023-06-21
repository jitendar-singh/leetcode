def ispalindrome(frames):
    output = []
    for farme in frames:
        if farme == farme[::-1]:
            output.append((farme,True))
        else:
            output.append((farme,False))
    return output

frames = ["tot", "pot", "bob", "rat", "tat"]
print(ispalindrome(frames))