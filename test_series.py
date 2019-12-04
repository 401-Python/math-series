# import pytest
from series import fibonacci, validate_input, lucas, sum_series

def test_validate_input_string():
  actual = validate_input('fart')
  expected = False
  assert actual == expected

def test_validate_input_good():
  actual = validate_input(2)
  expected = True
  assert actual == expected

def test_validate_input_below_zero():
  actual = validate_input(-1)
  expected = False
  assert actual == expected

def test_fibbonacci():
  actual = fibonacci(8)
  expected = 13
  assert actual == expected

def test_lucas():
  actual = lucas(8)
  expected = 29
  assert actual == expected

def test_sum_series():
  actual = sum_series(8)
  expected = 13
  assert actual == expected

def test_sum_series_with_param():
  actual = sum_series(8, 2)
  expected = 29
  assert actual == expected