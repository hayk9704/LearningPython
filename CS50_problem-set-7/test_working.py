import pytest
from working import convert

def main():
    test_PM()
    test_AM()
    test_text()

def test_text():
    with pytest.raises(ValueError):
        convert("text")
    with pytest.raises(ValueError):
        convert("tt:tt AM to mm:mm PM")
    with pytest.raises(ValueError):
        convert("10: 9 AM to 9:10 PM")

def test_AM():
    assert convert("10:00 AM to 5:00 PM") == "10:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 AM to 5:00 PM") == "10:30 to 17:00"
    assert convert("1:30 AM to 5:00 PM") == "01:30 to 17:00"
    assert convert("12:59 AM to 5:00 PM") == "00:59 to 17:00"
    with pytest.raises(ValueError):
        convert("13 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("12:67 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("121 AM to 5:00 PM")
    

def test_PM():
    assert convert("10:00 AM to 10:00 PM") == "10:00 to 22:00"
    assert convert("10:00 AM to 1:00 PM") == "10:00 to 13:00"
    assert convert("10:00 AM to 1:59 PM") == "10:00 to 13:59"
    assert convert("10:00 AM to 11:42 PM") == "10:00 to 23:42"
    assert convert("10:00 AM to 7 PM") == "10:00 to 19:00"
    with pytest.raises(ValueError):
        convert("10 AM to 55:00 PM")
    with pytest.raises(ValueError):
        convert("12 AM to 5:89 PM")
    with pytest.raises(ValueError):
        convert("12 AM to 112 PM")

if __name__ == "__main__":
    main()