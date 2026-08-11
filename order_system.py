from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price_cents: int

@dataclass
class LineItem:
    product: Product
    quantity: int
    @property
    def total_items(self):
        return self.quantity
    @property
    def subtotal(self) -> int:
        return self.product.price_cents*self.quantity

def discount(code:str=None):
    if code == "STAR10":
        return 10
    elif code == "STAR20":
        return 20
    elif code == "STAR25":
        return 25
    else:
        return 0


@dataclass
class Customer:
    name : str
    email: str

@dataclass
class Order:
    discount_code: str=None
    items: list[LineItem] = field(default_factory=list)

    def add_item(self,product:Product, quantity: int) -> None:
        self.items.append(LineItem(product,quantity))

    @property
    def total(self) -> float:
        raw_price = sum(item.subtotal for item in self.items)
        pct = discount(self.discount_code) if self.discount_code else 0
        discounted_cents = round(raw_price * (100 - pct) / 100)
        return discounted_cents / 100.0

    def __repr__(self):
        total_items = sum(item.quantity for item in self.items)
        return f"Order({total_items} items, INR {self.total:.2f})"


if __name__ == '__main__':
    order = Order("STAR10")
    order.add_item(Product("Book", 29900), 2)
    order.add_item(Product("Pen", 5000), 3)
    print(order)
    print(f"Total: INR {order.total:.2f}") 

# An Order uses composition ("has-a") because it is built out of independent component objects
# (Customer, LineItem), whereas Circle uses inheritance ("is-a") because a Circle is a specialized
# form of a generic Shape interface.