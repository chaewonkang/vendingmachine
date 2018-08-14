from vm import fibo

def test_1st_should_be_1():
    assert 1 == fibo(1)

def test_2nd_should_be_1():
    assert 1 == fibo(2)
