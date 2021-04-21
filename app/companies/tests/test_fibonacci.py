from utils.my_docorator import my_parametrize


@my_parametrize(identifiers="n,expected", values=[(0, 0), (1, 1), (2, 1), (20, 6765)])
def test_naive(n: int, expected: int) -> None:
    res = Fibonacci(n=n)
    assert res == expected
