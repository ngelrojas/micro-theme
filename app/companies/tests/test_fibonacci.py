import pytest
import json
from django.test import Client
from django.urls import reverse
from .my_decorator import my_parametrize, Fibonacci
from .test_fixtures import time_tracker

# fibonacci_url = reverse("fibonacci_view")


@my_parametrize(identifiers="n,expected", values=[(0, 0), (1, 1), (2, 1), (20, 6765)])
def test_naive(n: int, expected: int) -> None:
    # print(time_tracker)
    res = Fibonacci(n=n)
    assert res == expected


@my_parametrize(identifiers="n,expected", values=[(0, 0), (1, 1), (2, 1), (20, 6765)])
def test_view_fibonacci_convert_string(n: str, expected: int) -> None:
    n = int(n)
    resp = Fibonacci(n=n)
    assert resp == expected


# @pytest.mark.parametrize("n, expected", [(0, 0), (1, 1), (2, 1), (40, 102334155)])
# def test_n_number_success(client, n: str, expected: int) -> None:
#     response = client.get(path=f"/fibonacci?n={n}")
#     assert response.status_code == 200
#     assert json.loads(response.content) == {"data": expected}


# @pytest.mark.parametrize("n, expected", [("1", 1), ("1", 1)])
# def test_fibonnaci_numeric_string_should_pass(client, n: str, expected: int) -> None:
#     response = client.get(path=f"/fibonacci?n={n}")
#     assert response.status_code == 200
#     assert json.loads(response.content) == {"data": expected}


@pytest.mark.parametrize(
    "n, expected", [("a", "'a'"), (1.1, "'1.1'"), (True, "'True'")]
)
def test_fibonacci_invalid_types_should_fail(client, n: str, expected: int) -> None:
    with pytest.raises(ValueError) as e:
        client.get(path=f"/fibonacci?n={n}")
    assert f"invalid literal for int() with base 10: {expected}" == str(e.value)


# @pytest.mark.performance
# @track_performance
# def test_fibonacci_performance():
#     c = Client()
#     c.get(path=f"/fibonacci?n=10_100")
