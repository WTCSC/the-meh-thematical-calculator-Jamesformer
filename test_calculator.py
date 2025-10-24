import pytest
from calculator import addition, subtraction, multiplication, division
# testing for addition with both positive numbers and negative numbers
def test_add_numbers():
    assert addition(5, 5) == 10
def test_add_negative_numbers():
    assert addition(-7, -8) == -15


# testing subtraction through normal means and a small number against a big number
def test_subtraction_numbers():
    assert subtraction(56, 8) == 48
def test_subtraction_big_number():
    assert subtraction(32, 64) == -32

# testing multiplication normally and multiplying by 0
def test_multiplication_numbers():
    assert multiplication(5, 5) == 25
def test_multiplication_no_numbers():
    assert multiplication(5, 0) == 0



def test_division_numbers():
    assert division(56, 8) == 7
def test_division_singular_numbers():
    assert division(90, 1) == 90
def test_division_no_number_black_hole_generator():
    assert division(75, 0) == 0

