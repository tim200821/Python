
PurchasePrice = int(input("Purchase_price : "))

GiveMoney = int(input("Give_Money : "))

if GiveMoney > PurchasePrice:
    Building = GiveMoney - PurchasePrice
    print(f"Building {Building}")
else:
    print("Not enough money")

