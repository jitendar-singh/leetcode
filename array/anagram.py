
// it's anagram problem 
def anagram(s1: str,s2: str) -> bool:
    '''
    1- Remove all the white spaces\n
    2- Covert all charactres to lowercase\n
    3- Sort both strings\n
    4- Compare both strings for equality
    '''
    
    s1 = s1.replace(" ","")
    s2 = s2.replace(" ","")

    if(sorted(s1) == sorted(s2)):
        return True
    else:
        return False

def isAnagram(s1: str, s2: str)-> bool:
    count = {}
    s1 = s1.replace(" ","")
    s2 = s2.replace(" ","")
    for chars in s1:
        if chars in count:
            count[chars]+=1
        else:
            count[chars] = 1
    print(count)
    for chars in s2:
        if chars in count:
            count[chars]-=1
        else:
            count[chars]=1
    print(count)

    for k in count:
        if count[k]!=0:
            return False
    
    return True


result = anagram("clint eastwood","old west action")
print(result)
