from dataclasses import dataclass
from enum import Enum

class Category(Enum):
    ELECTRONICS="Electronics"
    CLOTHING="Clothing"
    FOOD="Food"

class OrderStatus(Enum):
    PENDING="Pending"
    CONFIRMED="Confirmed"
    SHIPPED="Shipped"
    DELIVERED="Delivered"

@dataclass
class Product:
    product_id:int
    name:str
    _price:float
    category:Category

    def __post_init__(self):
        if self._price <= 0:
            raise ValueError("Price must be greater than 0")
        
    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self,value:float):
        if value<=0:
            raise ValueError("price must be greater then zero")
        self.price=value

    def __str__(self):
        return f"{self.name} -> {self.price}"

class Shoppingcart:
    def __init__(self):
        self.products:list[Product]=[]

    def add_product(self,product:Product) -> None:
        self.products.append(product)

    def remove_product(self,product:Product) -> None:
        if product in self.products:
            self.products.remove(product)
        else:
            print("product is not in the cart")

    def total_price(self) -> float:
        return sum(product.price for product in self.products)

    def __len__(self) -> int:
        return len(self.products)

    def __contains__(self,product:Product) -> bool:
        return product in self.products

    def __str__(self):
        if not self.products:
            return "cart is empty"

        result="Shopping Cart:\n"

        for product in self.products:
            result+=f" - {product}\n"

        result+=f"Total:{self.total_price()}"
        return result


class Customer:

    def __init__(self,customer_id:int,name:str,email:str):
        self.customer_id=customer_id
        self.name=name
        self.email=email
        self.cart=Shoppingcart()

        def __str__(self):
            return f"Customer:{self.name}, Email:{self.email}"

class Order:

    def __init__(self, order_id: int, customer: Customer):
        self.order_id = order_id
        self.customer = customer

        self.products: list[Product] = customer.cart.products.copy()

        self.status = OrderStatus.PENDING

    @property
    def status(self) -> OrderStatus:
        return self._status

    @status.setter
    def status(self, value: OrderStatus):
        if not isinstance(value, OrderStatus):
            raise ValueError("Invalid order status")

        self._status = value

    def total_price(self) -> float:
        return sum(product.price for product in self.products)

    def __str__(self):
        return (
            f"Order ID: {self.order_id}\n"
            f"Customer: {self.customer.name}\n"
            f"Status: {self.status.value}\n"
            f"Total: ₹{self.total_price()}"
        )

laptop = Product(
    101,
    "Laptop",
    50000,
    Category.ELECTRONICS
)

shirt = Product(
    102,
    "Shirt",
    1500,
    Category.CLOTHING
)

pizza = Product(
    103,
    "Pizza",
    500,
    Category.FOOD
)


# Customer

customer = Customer(
    1,
    "Sneha",
    "sneha@example.com"
)


# Add products

customer.cart.add_product(laptop)
customer.cart.add_product(shirt)
customer.cart.add_product(pizza)


# Display cart

print(customer)
print()

print(customer.cart)
print()


# len(cart)

print("Number of products:", len(customer.cart))


# product in cart

print("Laptop in cart:", laptop in customer.cart)


# Total price

print("Total price:", customer.cart.total_price())


# Remove product

customer.cart.remove_product(shirt)

print()
print("After removing shirt:")
print(customer.cart)


# Create order

order = Order(1001, customer)

order.status = OrderStatus.CONFIRMED

print()
print("----- ORDER -----")
print(order)