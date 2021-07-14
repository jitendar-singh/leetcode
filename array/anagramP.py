def anagramP(l1: str,l2: str)-> bool:
    l1 = l1.lower()
    l2 = l2.lower()
    l1 = l1.replace(" ","")
    l2 = l2.replace(" ", "")

    print(l1)
    print(l2)
    # return sorted(l1) == sorted(l2)
    seen = {}
    for chars in l1:
        if chars in seen:
            seen[chars]+=1
        else:
            seen[chars]=1
    print(seen)

    for chars in l2:
        if chars in seen:
            seen[chars]-=1
        else:
            seen[chars]=1
    
    for k in seen:
        if seen[k]!=0:
            return False
    return True
    

            

a = "su nn y"
b = "Sunny"
result = anagramP(a,b)
print(result)