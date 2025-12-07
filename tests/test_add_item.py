import pytest

from source.ecart import Ecart

@pytest.fixture
def cart():
    return Ecart()

def test_add_single_item_success(cart):
    #Adding one valid item should add it to the cart.
    cart.add_item("Apple", 2.5, 3)

    assert len(cart.items) == 1
    assert cart.items[0]["item"] == "Apple"
    assert cart.items[0]["price"] == 2.5
    assert cart.items[0]["quantity"] == 3

def test_add_single_item_price_less_than_0(cart):
    #should raise value error
    with pytest.raises(ValueError, match="Quantity must be greater than zero"):
        cart.add_item("Orange", 1, 0)

#def test_add_multiple_items(cart):
    #adding different items to the cart

