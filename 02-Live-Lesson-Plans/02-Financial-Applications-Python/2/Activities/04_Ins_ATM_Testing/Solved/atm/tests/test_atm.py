"""Script to test ATM functionality."""


from utils import validate_pin


# Test to validate PIN
def test_validate_pin():
    assert validate_pin("123456") == True
