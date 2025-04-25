from bank import value
import pytest

def main():
    test_value_0()
    test_value_20()
    test_value_100()

def test_value_0():
    assert value("a") == 0
    assert value("fam") == 0
    assert value("bam") == 0
    assert value("alasa") == 0
    assert value("099k") == 0
    assert value("mklo") == 0
    assert value("qwe") == 0

def test_value_20():
    assert value("ha") == 20
    assert value("he") == 20
    assert value("holi") == 20
    assert value("hiio") == 20

def test_value_100():
    assert value("hello") == 100
    assert value("hellomino") == 100
    assert value("hellop") == 100
    assert value("hello?") == 100