# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing Started")

for item in inventory:
    print(f"Processing {item}")
    current_stock, min_stock, restock_quantity, sale_status = inventory[item]


    while current_stock < min_stock:
        current_stock += restock_quantity
    inventory[item][0] = current_stock
    if current_stock > discount_threshold:
        sale_status = True
    else:
        sale_status = False
    inventory[item][3] = sale_status

print("Processing completed")
    
        
        