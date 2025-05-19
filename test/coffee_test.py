from customer import Customer
from coffee import Coffee
from order import Order

def test_coffee_properties():
    c = Coffee("Espresso")
    assert c.name == "Espresso"

def test_coffee_orders_and_customers():
    c1 = Coffee("Cappuccino")
    cust1 = Customer("Ella")
    cust2 = Customer("Max")
    Order(cust1, c1, 4.5)
    Order(cust2, c1, 6.0)

    assert c1.num_orders() == 2
    assert len(c1.customers()) == 2
    assert c1.average_price() == 5.25
