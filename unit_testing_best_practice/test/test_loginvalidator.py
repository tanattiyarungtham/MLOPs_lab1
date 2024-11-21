import sys
# Always run from unit_testing_best_practice/test
sys.path += ['../src'] 

from sample_loginvalidator import *

def test_validate_username():
    assert validate_username("user123") == True  # Valid username
    assert validate_username("") == False        # Empty username
    assert validate_username("user name") == False  # Contains spaces

def test_validate_password():
    assert validate_password("Passw0rd!") == True  # Valid password
    assert validate_password("short") == False     # Too short
    assert validate_password("password") == False  # No number
    assert validate_password("12345678") == False  # No letter
    assert validate_password("Passw0rd") == False  # No special character

def test_validate_email():
    assert validate_email("user@example.com") == True  # Valid email
    assert validate_email("userexample.com") == False  # Missing @
    assert validate_email("user@examplecom") == False  # Missing .
    assert validate_email("user@.com") == False        # Invalid placement of .
 
