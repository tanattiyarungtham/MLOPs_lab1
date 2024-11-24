import sys
# Always run from unit_testing_best_practice/test
sys.path += ['../src'] 

from calculator import *

def test_addition():
    assert addition(1,2) == 3
    assert subtraction(2,1) == 1
    assert multiplication(1,2) == 2
    assert division(2,1) == 2
 