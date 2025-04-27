import pytest
from numb3rs import validate

def main():
    test_text()
    test_digits()
    

def test_digits():
    assert validate("255.255.255.255") == True
    assert validate("256.256.256.256") == False
    assert validate("255.196.29.3") == True
    assert validate("2.12.45.122") == True
    assert validate("0.6.6.189") == True
    assert validate("01.04.09.67") == False

def test_text():
    assert validate("cat") == False
    assert validate("d.256.256.256") == False
    assert validate("255.196.sad.3") == False
    assert validate("2.12.45.asd") == False
    assert validate("0.6asd.6.189") == False
    assert validate("01.04ff.a.67") == False

if __name__ == "__main__":
    main()