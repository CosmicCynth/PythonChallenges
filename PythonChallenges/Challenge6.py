#Create a function that takes two arguments:
#the original price and the discount percentage as integers and returns the final price after the discount.

def FindTheDiscount(price,discount):
    FinalPrice = price*discount
    FinalPrice = round(FinalPrice,2)
    return FinalPrice

print("Final price: " + str(FindTheDiscount(798,0.65)))
