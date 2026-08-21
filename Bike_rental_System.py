class BikeShop:
    def __init__(self, stoke):
        self.stoke = stoke
    def displaybike(self):
        print("Total Bikes:", self.stoke)
    def rentbike(self, quantity):

        if quantity <= 0:
            print("Enter positive value greater than 0:")
        elif quantity > self.stoke:
            print("Enter value less than stoke:")
        else:
            self.stoke = self.stoke - quantity
            print("Total Price: ",quantity*100)
            print("Total available Bikes: ", self.stoke)

while True:
    obj = BikeShop(50)
    #uc means user choice
    uc = int(input('''                    
    1. Display available stoke
    2. Request a bike for rent (100 Rs--> quantity)
    3. Exit 
    
    '''))
    if uc == 1:
        obj.displaybike()
    elif uc == 2:
        n = int(input("Enter bikes Quantity: "))
        obj.rentbike(n)
    else:
        break




