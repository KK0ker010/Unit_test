import pytest
from age import categorize_by_age

def test_age_Child():
    assert categorize_by_age(3) == "Child"
    assert categorize_by_age(9) == "Child"

def test_age_Teenager():
    assert categorize_by_age(14) == "Teenager"
    assert categorize_by_age(18) == "Teenager"

def test_age_Adult():
    assert categorize_by_age(43) == "Adult"
    assert categorize_by_age(64) == "Adult"

def test_age_Golden_Age():
    assert categorize_by_age(65) == "Golden Age"
    assert categorize_by_age(120) == "Golden Age"

def test_age_Invalid_Age():  
    assert categorize_by_age(121) == "Invalid Age: 121"
    assert categorize_by_age(-121) == "Invalid Age: -121"
    assert categorize_by_age(-1) == "Invalid Age: -1"