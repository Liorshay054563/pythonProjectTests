import pytest
import calculator


def test_calculator_add():
    # Arrange
    a: int = 2
    b: int = 5
    expected: int =7

    # act
    actual : int = calculator.add(a,b)

    # assert
    assert expected == actual , "small numbers add check"

def test_calculator_minus():
    a: int = 12
    b: int = 5
    expected: int = 7

    # act
    actual: int = minus(a, b)

    # assert
    assert expected == actual, "small numbers minus check"
