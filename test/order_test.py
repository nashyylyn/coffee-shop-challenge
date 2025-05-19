from customer import Customer
from coffee import Coffee
from order import Order

def test_order_validation():
    c = Customer("Liam")
    coffee = Coffee("Americano")
    
    o = Order(c, coffee, 7.5)
    assert o.customer == c
    assert o.coffee == coffee
    assert o.price == 7.5
