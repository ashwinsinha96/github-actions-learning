from app import add, subtract


def test_add():
    assert add(10, 20) == 30


def test_add_negative():
    assert add(-5, 5) == 0


def test_subtract():
    assert subtract(20, 10) == 10


def test_subtract_negative():
    assert subtract(5, 10) == -5