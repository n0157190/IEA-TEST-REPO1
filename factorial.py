comp = int(input("Enter a number: "))
ttl = 1
for i in range(1,comp):
    ttl += ttl * (comp -1)
    comp -= 1
print("Your total is: ", ttl)