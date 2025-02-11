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
    actual: int = calculator.minus(a, b)

    # assert
    assert expected == actual, "small numbers minus check"

def test_calculator_multiply():
    a: int = 10
    b: int = 5
    expected: int = 50

    # act
    actual: int = calculator.multiply(a,b)

    # assert
    assert expected == actual, "small numbers multiply check"

def test_calculator_divide():
    a: int = 10
    b: int = 5
    expected: int = 2

    # act
    actual: int = calculator.divide(a, b)

    # assert
    assert expected == actual, "small numbers divide check"

def test_calculator_power():
    # Arrange
    a: int = 2
    b: int = 4
    expected: int = 16

    # act
    actual: int = calculator.power(a,b)

    assert actual == expected , "small numbers power by check"

def test_calculator_power2():
    # Arrange
    a: int = 3
    b: int = 2
    expected: int = 9

    # act
    actual: int = calculator.power(a, b)

    assert actual == expected, "small numbers power by check"

def test_calculator_sqrt():
    # Arrange
    a: int = 25
    expected: int = 5

    # act
    actual: int = calculator.sqrt(a)

    assert actual == expected, "small number sqrt check"


def test_calculator_sqrt_negative():
    # Arrange
    a: int = -5

    with pytest.raises(ValueError) as ex:
        calculator.sqrt(a)

def test_calculator_factorial():
    # Arrange
    a: int = 4
    expected: int = 24

    # act
    actual: int = calculator.factorial(a)

    assert actual == expected, "small number factorial check"

def test_calculator_factorial2():
    # Arrange
    a: int = 5
    expected: int = 120

    # act
    actual: int = calculator.factorial(a)

    assert actual == expected, "small number factorial check"

def test_calculator_factorial_negative_num():
    # Arrange
    a: int = -3

    with pytest.raises(ValueError) as ex:
        calculator.factorial(a)




