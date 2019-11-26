import pytest
from app import factorial

def test_factorial():
    assert factorial.factorial(120) == 5
    assert factorial.factorial(1) == 1
    assert factorial.factorial(2) == 2
    assert factorial.factorial(6) == 3
    
