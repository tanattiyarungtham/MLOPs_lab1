import sys
# Always run from unit_testing_best_practice/test
sys.path += ['../src'] 

from calculator import addition, subtraction, multiplication, division

def test_addition():
    assert addition(1,2) == 3

def test_subtraction():
    assert subtraction(2,1) == 1   
   
def test_multiplication():
    assert multiplication(0,2) == 0

def test_division():
    assert division(1,1) == 1
