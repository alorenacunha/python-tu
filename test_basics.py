def helloWorld():
    return 'hello world'

def inc(x):
    return x + 1


def test_hello_world():
    assert helloWorld() == 'hello world' 

def test_inc():
    assert inc(3) == 4