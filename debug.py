from customer import Customer
from coffee import Coffee
from order import Order


alice = Customer("Alice")
bob = Customer("Bob")
carol = Customer("Carol")


latte = Coffee("Latte")
mocha = Coffee("Mocha")


alice.create_order(latte, 5.0)
alice.create_order(mocha, 6.0)
bob.create_order(latte, 4.5)
carol.create_order(latte, 7.0)
carol.create_order(mocha, 5.5)


print(f"Alice's orders: {alice.orders()}")
print(f"Alice's coffees: {[coffee.name for coffee in alice.coffees()]}")
print(f"Latte orders: {latte.orders()}")
print(f"Customers who ordered Mocha: {[c.name for c in mocha.customers()]}")
print(f"Number of Latte orders: {latte.num_orders()}")
print(f"Average price for Latte: {latte.average_price():.2f}")


most_spent = Customer.most_aficionado(latte)
if most_spent:
    print(f"The most aficionado for Latte is: {most_spent.name}")
else:
    print("No aficionado for Latte.")
