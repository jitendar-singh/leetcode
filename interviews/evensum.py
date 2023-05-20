# Implement a Python function that takes in a list of integers and returns the sum of all the even numbers in the list.
def evenSum(mylst):
    sum = 0
    for item in mylst:
        if item % 2 == 0:
            sum+=item
    return sum

mylst = [0,2,3,4,6,5,7,8]
sum = evenSum(mylst)
print(sum)