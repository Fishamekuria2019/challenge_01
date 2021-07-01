from utils import validate_pin
from actions.make_withdrawal import make_withdrawal

def test_validate_pin():
    assert validate_pin("123456") == True

def test_make_withdrawal():
    assert make_withdrawal({"pin":123456, "balance":325.20}, 10.25) != False
