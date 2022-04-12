# Python script for applying supermarket pricing.
import string
testa = int(input("Enter how many 3 for 1$ items in your cart: "))
testb = input("Enter how many lbs and oz your cart ex 2, 8: ")
testb = testb.split(', ')

def three_for_dollar(qty):
    unit_price = .333
    # add a penny to the total for every 3 units purchased.  Not sure what to do with remainders
    total = unit_price * qty + qty/3 * .01 
    print (f"With {qty} items, three for a dollar total price: $", round(total,2), "Unit price: ")

def per_pound(lbs, ounces):
    # price per lb
    unit_price = 1.99
    ounce_price = 1.99/16
    print(f"ounce_price: {ounce_price}")
    total = round(lbs * unit_price + ounces * ounce_price, 2)
    #print ('total: ', total, round(total, 2))
    print(f"At $1.99/lb, total price for {lbs} lbs and {ounces} oz: ${total}")


three_for_dollar(testa)
per_pound(int(testb[0]), int(testb[1]))

