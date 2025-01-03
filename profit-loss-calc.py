cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

if cost_price > selling_price:
    print("This is a loss.")
    loss = cost_price - selling_price
    loss_percentage = (loss / cost_price) * 100
    print("The calculated loss is equal to: ", loss)
    print("The calculated percentage loss is equal to: ", loss_percentage)
if selling_price > cost_price:
    print("This is a profit.")
    profit = selling_price - cost_price
    profit_percentage = (profit / cost_price) * 100
    print("The calculated profit is equal to: ", profit)
    print("The calculated Percentage Profit (%) is equal to: ", profit_percentage)
else:
    print("Neither a profit or loss.")