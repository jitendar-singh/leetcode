# FizzBuzz: Write a Python program that prints the numbers from 1 to 100. 
# But for multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz". 
# For numbers that are multiples of both three and five, print "FizzBuzz".

def fizzbuzz():
    for num in range(1,100):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        if num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Bizz")
        else:
            print(num)

if __name__ == "__main__":
    fizzbuzz()
