from app.math_utils import add, subtract

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 4) == 6  # ← This is intentionally broken

