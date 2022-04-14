

def fizzbuzz(n):
    flag = 0
    if n % 3 == 0 and n % 5 == 0:
        print ("FizzBuzz")
        flag = 1
    if n % 3 == 0 and flag != 1:
        print ("Fizz")
        flag = 1
    if n % 5 == 0 and flag != 1:
        print("Buzz")
        flag = 1
    if flag != 1:
        print (n)
    if n == 100:
        quit()
    fizzbuzz(n = n +1)

fizzbuzz(1)