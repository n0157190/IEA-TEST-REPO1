from math import log

history = []

class Calculator(object):
    def __init__(self):
        self.balance = 0

    def add(self, *args):
        for num in args:
            self.balance += num
            history.append('Added '+ str(num))
        return self.balance
        
    def sub(self, *args):
        for num in args:
            self.balance -= num
            history.append('Subtracted '+ str(num))
        return self.balance
    
    def mult(self, *args):
        if len(args) > 1:
            self.balance = args[0] * args[1]
            history.append('Mult '+ str(args[0]) + ' ' + str(args[1]))
        else:
            self.balance = self.balance * args[0]
            history.append('Mult '+ str(self.balance) + ' ' + str(args[0]))
        return self.balance
            
    def div(self, *args):
        if len(args) > 1:
            self.balance = args[0] / args[1]
            history.append('Div '+ str(args[0]) + ' ' + str(args[1]))
        else:
            self.balance = self.balance / args[0]
            history.append('Div '+ str(self.balance) + ' ' + str(args[0]))
        return self.balance
        
    def showcalc(self):
        for trans in history:
            print(trans)
        return

    def ac():
        self.balance = '0.0'
        return self.balance