
from src.functions.basics import helloWorld, inc

def test_hello_world():
    assert helloWorld() == 'hello world' 

def test_inc():
    assert inc(3) == 4