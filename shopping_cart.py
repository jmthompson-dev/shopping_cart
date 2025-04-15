
class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${int(total)}")

items = []

num_items = int(input("How many items would you like to add to your cart?\n"))

for i in range(num_items):
    print(f"\nItem {i + 1}")
    item = ItemToPurchase()
    item.item_name = input("Enter the item name:\n")
    item.item_price = float(input("Enter the item price:\n"))
    item.item_quantity = int(input("Enter the item quantity:\n"))
    items.append(item)

print("\nTOTAL COST")
total_cost = 0

for item in items:
    item.print_item_cost()
    total_cost += item.item_price * item.item_quantity

print(f"\nTotal: ${int(total_cost)}")
