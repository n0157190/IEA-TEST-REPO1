
# Display prime numbers within a range

lower = 20
upper = 40
irange = [lower, upper]

def prime(l,u):
    for num in range(l, u + 1):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

print("Prime numbers between", lower, "and", upper, ":")
prime(irange[0], irange[1])