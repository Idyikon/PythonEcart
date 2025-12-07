
class EmptyCart(Exception):
    pass


class Ecart:

    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            raise ValueError("Your Cart is empty")

    # add an item if item count is 1 or more
    def add_item(self, item, price, quantity=1):

        if price <= 0:
            raise ValueError("Price must be greater than zero.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        self.items.append({
                "item": item,
                "price": price,
                "quantity": quantity
        })

    def total(self):
        return sum(i["price"] * i["quantity"] for i in self.items)

    def remove_item(self, item, price, quantity=1):
        #  Check if the cart is empty
        self.is_empty()

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        # Find the item in the cart
        item_exists = next((i for i in self.items if i["item"] == item), None)

        if not item_exists:
            raise ValueError(f"{item} is not in the cart.")

        # Reduce the quantity
        if item_exists["quantity"] < quantity:
            raise ValueError("Cannot remove more than the existing quantity.")

        item_exists["quantity"] -= quantity

        # If quantity drops to zero, remove it completely
        if item_exists["quantity"] == 0:
            self.items.remove(item_exists)

        return f"Removed {quantity} of {item}."


    def __repr__(self):
        return f"Ecart({self.items})"

