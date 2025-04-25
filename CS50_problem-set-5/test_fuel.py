import pytest
from fuel import convert, gauge

def main():
    test_zerodiv()
    test_valueerror()
    test_correct()
    test_gauge()

def test_zerodiv():
    with pytest.raises(ZeroDivisionError):
        convert("10/0")

def test_valueerror():
    with pytest.raises(ValueError):
        convert("10/8")
    with pytest.raises(ValueError):
        convert("10/am")

def test_correct():
    assert convert("9/10") == 90
    assert convert ("1000/1001") == 100

def test_gauge():
    assert gauge(10) == "10%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"