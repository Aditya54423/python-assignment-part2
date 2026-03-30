#------------------------------------------
#PART-2 DATA STRUCTURES
#THEME : RESTAURANT MANAGEMENT SYSTEM
#-------------------------------------------
import copy # It is given in question and will be required for Task copy 

#-------------DATA PROVIDED----------------------
menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}

#------------------------------------
#TASK 1 - EXPLORE THE MENU
#----------------------------------------
print("\n" + "=" * 40)
print("     TASK 1: FULL MENU")
print("=" * 40)

#Here we will need to group by category . Rahter than hardcoding the categories,
#Here I'll collect them from the data itself 
categories = []
for item_info in menu.values():
    cat = item_info["category"]
    if cat not in categories:     #this will preserve the order they first appear
        categories.append(cat)


for cat in categories:
    print(f"\n===={cat}===")
    for item_name,item_info in menu.items():
        if item_info["category"]==cat:
            tag = "[Available]" if item_info ["available"] else "[Unavailable]"
            #:<16 pads name so prices line up  and align nicely
            print(f"{item_name:<16} ₹{item_info['price']:.2f} {tag}")
 
 
 # Dictionary method stats
total_items  =len(menu)
available_items = sum(1 for v in menu.values() if v ["available"])           
  
# Most expensive: here we will walk through all items tracking the highest price seen
top_item = None
top_price = 0.0
for name,info in menu.items():
    if info["price"] > top_price:
        top_price = info["price"]
        top_item = name

# Items under ₹150
cheap_items = [(n,i["price"]) for n,i in menu.items() if i["price"]<150]

print(f"\n Total items on menu  : {total_items}")
print(f" Available items : {available_items}")
print(f" Most expensive item. : {top_item} (₹{top_price:.2f})")
print(f" Items priced under ₹150:")
for name,price in cheap_items:
    print(f"  .{name} - ₹{price:.2f}")



#------------------------------------------------------------
#TASK -2 CART OPERATIONS
#------------------------------------------------------------    
print("\n\n" + "=" * 40)
print("   TASK 2: CART OPERATIONS") 
print("="* 40)

cart =[] #This is there for each entry :("item": str),"quantity":int,"price": float

def print_cart(label = "Cart State"):
    print(f"\n [{label}]")
    if not cart:
        print(" (cart is empty)")
        return
    for entry in cart:
        print(f"  {entry['item']}  x{entry['quantity']} ₹{entry['price'] * entry['quantity']:.2f}")  


def add_item(item_name,qty):
    #Case 1 :- If the item does not exist at all
    if item_name not in menu:
     print(f"\n x '{item_name}' is not found in the menu")   
     return
    
    #Case 2:- If the item is available today or not ?
    if not menu[item_name]['available']:
        print(f"\n x '{item_name}' is currently unavailable.")
        return      
    
    #Now we will put a check to see if it's already sitting in the cat somewhere
    #For this I will approach by scanning through the entire cart entries looking for a name match
    for entry in cart :
        if entry["item"] == item_name:
            entry["quantity"]+= qty
            print(f"\n ✓ Updated '{item_name}' quantity to {entry['quantity']}. ")
            return
    
    # If not found in cart yet then we will add a fresh entry
    cart.append({
        "item":  item_name,
        "quantity": qty,
        "price": menu[item_name]["price"]})
    print(f"\n ✓Added '{item_name}' x{qty} to cart.")
    

def remove_item(item_name):
    for i,entry in enumerate(cart):
        if entry["item"] == item_name:
            cart.pop(i)
            print(f"\n ✓ Removed '{item_name}' from the cart.")
            return
    print(f"\n x '{item_name}' is not in the cart.")


def update_quantity(item_name,new_qty):
    for  entry in cart:
        if entry['item']== item_name:
            entry["quantity"] = new_qty
            print(f"\n ✓'{item_name}' quantity updated to {new_qty}.")
            return
    print(f"\n x '{item_name}")    
    

# Now we will try to make the order sequence
add_item("Paneer Tikka",2)
print_cart("After adding Paneer Tikka x2")

add_item("Gulab Jamun",1)
print_cart("After adding Gulab Jamun x1")

add_item("Paneer Tikka",1)       #Here as we can see Paneer Tikka is ordered again so it should be update qty to 3 and not duplicate it.
print_cart("After adding Paneer Tikka x1 again (expect qty = 3)")

add_item("Mystery Burger",1)         #Here we can see that the Mystery Burger was ordered that  doesn't even exist in the menu.
print_cart("After trying Mystery Burger")

add_item("Chicken Wings",1)            # Now Chicken wings are in the menu but right now it's unavailable
print_cart("After trying Chicken Wings")

remove_item("Gulab Jamun")    #Here the customer previously ordered gulab jamun and now removed it from the order.
print_cart("After removing Gulab Jamun")

# Now we will build a "FINAL ORDER SUMMARY" on the basis of the items previously ordered above and the customer will be billed for it.
subtotal = sum(e["price"] * e["quantity"] for e in cart)
gst = round(subtotal* 0.05,2)
total = round(subtotal + gst,2)

print("\n --------Order Summary---------")
for entry in cart :
    line_total = entry["price"] * entry["quantity"]
    print(f" {entry['item']:<18} x{entry['quantity']}  ₹{line_total:.2f}")
print(" ----------------------------------")   
print(f" {'Subtotal:' :<28} ₹{subtotal:.2f}") 
print(f" {'GST (5%):' :<28} ₹{gst:.2f}")
print(f" {'Total Payable:':<28} ₹{total:.2f}")
print("------------------------------")

#----------------------------------------------
#INVENTORY TRACKER WITH DEEP COPY
#-----------------------------------------------
print("\n\n" + "=" * 40)
print(" TASK 3 : INVENTORY TRACKER")
print("=" * 40)

#We will first use deepcopy
inventory_backup = copy.deepcopy(inventory)
print("\n [Deep Copy working]") #Using this as a check if deepcopy is there so that it would be easier for me to understand 
inventory["Garlic Naan"]["stock"] = 999     #this would be treated as a fake change for me
print(f"  inventory['Garlic Naan']['stock']  = {inventory['Garlic Naan']['stock']}")
print(f"  inventory_backup['Garlic Naan'] ['stock']   = {inventory_backup['Garlic Naan']['stock']}")
print("  Backup is unaffected.  ✓")

#Now we will try to restore the original value before proceeding futher
inventory["Garlic Naan"]["stock"] = 30

#Now we will try to deduct cat quantities from inventory
print("\n [Deducting cart from inventory]")
for entry in cart :
       item_name = entry["item"]
       qty_needed = entry["quantity"]
       current_stock = inventory[item_name]["stock"]
    
       if current_stock >= qty_needed:
        inventory[item_name]["stock"] -= qty_needed   
        print(f"✓ {item_name}: {current_stock} -> {inventory[item_name]['stock']}")
       else:
           # Now we want that the values should not go negative and only deduct from what's there
           print(f" {item_name}: only {current_stock} in stock , needed {qty_needed}. Deducting {current_stock}.")
           inventory[item_name]["stock"] = 0
           
# NOW WE WILL REORDER ALERTS
print("\n [Reorder Alerts]")  
alert_found = False
for item_name,data in inventory.items():
    if data["stock"]<= data["reorder_level"]:
        print(f" ! Reorder Alert : {item_name} -> Only {data['stock']} unit(s) left"
              f"(reorder_level : {data['reorder_level']})")  
        alert_found =True
if not alert_found:
    print("  No restocking required,All items are sufficiently stocked.")   

# Now a check that backup will differ from current inventory
print("\n [Comparing inventory vs backup for cart items]")  
for entry in cart:
    n = entry["item"]
    print(f"{n}: inventory={inventory[n]['stock']}, backup = {inventory_backup[n]['stock']}")  
    print(" -> they do differ, hence deep copy protected the original data . ✓")            
    
#--------------------------------
#TASK 4 DAILY SALES LOG ANALYSIS
#--------------------------------
print("\n\n" + "=" * 40)
print("   TASK 4 : SALES LOG ANALYSIS")
print("=" * 40)

def print_revenue_table(log):
    #This code can be reused multiple times to print revenue per day and also returns the best day
    print(f"\n {'Date': <14}| {'Orders':>6} | {'Revenue': >10}")
    print(" " + "-" * 36)   
    best_day = None
    best_revenue = 0.0  
    
    for date,orders in log.items():
      day_revenue = sum(o["total"] for o in orders)
      print(f"\n {date: <14}| {len(orders):>6} | ₹{day_revenue: >9.2f}")
      if day_revenue > best_revenue:
        best_revenue = day_revenue
        best_day = date
        
    print(f"\n Best-selling day :{best_day} (₹{best_revenue: .2f})")         
    return best_day        

print("\n Before adding new day ")
print_revenue_table(sales_log)

#Now we will look for the most ordered items for this I will approach by building a dictionary where item_name
# how may orders it appears in
item_order_count ={}
for orders in sales_log.values():
    for order in orders:
        for item in order["items"]:
            item_order_count[item] = item_order_count.get(item,0)+1


#  Now Finding the item with the highest count
most_ordered = None
most_ordered_freq = 0
for item,count in item_order_count.items():
    if count > most_ordered_freq:
        most_ordered_freq = count
        most_ordered = item

print(f"\n Most ordered item : {most_ordered} (reflects in {most_ordered_freq} orders)")        
          
# now for adding new day and reprint
sales_log["2025-01-05"] = [
    {"order_id": 11 , "items": ["Butter Chicken","Gulab Jamun", "Garlic Naan"], "total":490.0},
     {"order_id":12,"items": ["Paneer Tikka","Rasgulla"], "total": 260.00},    
]

print("\n After adding 2025-01-05")
print_revenue_table(sales_log)

# Now I will make a numbered lists of ALL orders using enumerate
print("\n [All orders : Numbered]")
counter = 1
for date,orders in sales_log.items():
    for order in orders:
        items_str = ",".join(order["items"])
        print(f"{counter:<3} [{date}] Order #{order['order_id']:<3}"
        f" -> ₹{order['total']:.2f} - Items: {items_str}")
        counter += 1
print("\n" + "=" * 40) 
print("  ALL TASKS COMPLETED")
print("=" *40+ "\n")       