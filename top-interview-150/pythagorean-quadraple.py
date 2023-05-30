def find_pythagorean_quadraple(number):
    quadraples = []
    for a in range(1, number):
        for b in range(a,number):
            for c in range(b, number):
                d_square = a ** 2 + b ** 2 + c ** 2
                d = int(d_square ** 0.5)
                if d ** 2 == d_square and d < number:
                    quadraples.append((a,b,c,d))
    return quadraples

result = find_pythagorean_quadraple(10)
for quadraple in result:
    print(str(quadraple).replace('(', '').replace(')','').replace(',',''))
    # print(quadraple)
