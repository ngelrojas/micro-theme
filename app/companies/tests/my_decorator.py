from typing import List, Tuple, Callable, Dict


def Fibonacci(n):

    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        return 0

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


Decorator = Callable


def get_list_of_for_function(
    identifiers: str, values: List[Tuple[str, str]]
) -> List[Dict[str, str]]:
    print(f"getting list of kwargs for function, \n{identifiers=}, {values=}")
    parsed_identifiers = identifiers.split(",")
    list_of_kwargs_for_function = []
    for tuple_value in values:
        kwargs_for_function = {}
        for i, keyword in enumerate(parsed_identifiers):
            kwargs_for_function[keyword] = tuple_value[i]
        list_of_kwargs_for_function.append(kwargs_for_function)
    print(f"{list_of_kwargs_for_function=}")
    return list_of_kwargs_for_function


def my_parametrize(identifiers: str, values: List[Tuple[int, int]]) -> Decorator:
    def my_parametrized_decorator(function: Callable) -> Callable:
        def run_func_parametrized() -> None:
            list_of_kwargs_for_function = get_list_of_for_function(
                identifiers=identifiers, values=values
            )
            for kwargs_for_function in list_of_kwargs_for_function:
                print(
                    f"calling function {function.__name__} with {kwargs_for_function=}",
                    function(**kwargs_for_function),
                )

        return run_func_parametrized

    return my_parametrized_decorator
