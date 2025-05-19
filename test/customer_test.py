from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_validation():
    try:
        Customer("")
    except ValueError:
        pass

    try:
        Customer("a" * 16)
    except ValueError:
        pass

    assert Customer("Jane").name == "Jane"

def test_customer_orders_and_coffees():
    c = Customer("Anna")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Mocha")
    c.create_order(coffee1, 5.0)
    c.create_order(coffee2, 6.0)
    c.create_order(coffee1, 5.5)

    assert len(c.orders()) == 3
    assert len(c.coffees()) == 2
