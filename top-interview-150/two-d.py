def count_ones(matrix):
    count, i = {}, 0
    for row in matrix:
        ctr = 0
        for column in row:
            if column == 1:
                ctr= ctr+1
                count[i]=ctr
        i+=1
    return max(count.keys())

matrix = [[0,0,1,0],[1,0,1,0],[1,0,0,1],[1,0,1,1],[1,1,1,1]]
row = count_ones(matrix)
print(f'Row with the maximum 1s is {row}')