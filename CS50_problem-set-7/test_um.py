from um import count

def main():
    test_signs()
    test_text()
    test_amount()

def test_signs():
    assert count("um,") == 1
    assert count("um..") == 1
    assert count("..um") == 1
    assert count("-um") == 1

def test_text():
    assert count("hum") == 0
    assert count("humu") == 0
    assert count("umu") == 0


def test_amount():
    assert count("um, none, um") == 2
    assert count("um. um. um... um?") == 4
