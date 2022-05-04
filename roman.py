roman = {'M' : 1000, 'D' : 500, 'C' : 100, 'L' : 50, 'X' : 10, 'V' : 5, 'I' : 1}
r = roman.values()
print(sum(r))
#rn = 'MCDXCII' MCMLXIX
rn = input("Enter a Roman Numeral for conversion: ").upper()
total = 0
x = 1000
for i in rn:    
    if (roman[i] <= x):
        total += roman[i]
        #print("+++", roman[i], total)
    else:
        total += roman[i] - (x*2)
        #print("---", roman[i], total)
    x = roman[i]
print(total)