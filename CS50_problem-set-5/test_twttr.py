import pytest
from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("lama") == "lm"
    assert shorten("aeoui") == ""
    assert shorten("qwertasdfzxcv") == "qwrtsdfzxcv"