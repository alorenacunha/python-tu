
from src.functions.basics import helloWorld, inc
import pytest

def test_hello_world():
    """test hello_world"""
    assert helloWorld() == 'hello world' 
    """test string diferente"""
    assert helloWorld() != 'não hello world' 
    """test int to hello world"""
    assert helloWorld() != 1 

def test_inc():
    """test negative int"""
    assert inc(-3) == -2
    """test int"""
    assert inc(3) == 4
    """test 0"""
    assert inc(3) == 4
    """test wrong"""
    assert inc(3) != 5
    """test boolean"""
    assert inc(True) == 2
    """test string"""
    with pytest.raises(TypeError):
        inc('3')