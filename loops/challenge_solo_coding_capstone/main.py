# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}

#looping through each item in the inventory dictionary and seperating out the things within the items in the dictionary
for item in inventory:
    print(f"Processing {item}")
    current_stock, reg_price, discounted_price = inventory[item]
    #print statement for items needing to be sold at discounted_price
    if current_stock < 30:
        print(f"{item} need restocking.")
    elif current_stock > 100:
        print(f"{item} should be sold at the discounted price of {discounted_price}.")
    else:
        print(f"{item} should be sold at the regular price of {reg_price}.")
    
        