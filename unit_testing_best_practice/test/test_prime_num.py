import sys
# Always run from unit_testing_best_practice/test
sys.path += ['../src'] 

from prime_num import *

def test_is_prime():
    assert is_prime(1) == False
    assert is_prime(3) == True
    assert is_prime(4) == False

