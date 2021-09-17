
def helloWorld():
    return 'hello world'

def inc(x):
    print(isinstance(x,int))
    if(isinstance(x,int) == False):
        raise TypeError("parameter has to be a int")
    return x + 1