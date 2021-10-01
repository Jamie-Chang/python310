from typing import Callable, Iterable, Iterator, ParamSpec, TypeAlias, TypeVar, Union

from contextlib import contextmanager


# PEP 604

uid: Union[int, str] = 1

uid: int | str = 2

print(isinstance(uid, str | int))


# PEP 612


@contextmanager
def cm(value: int) -> Iterator[int]:
    yield value


P = ParamSpec("P")
T = TypeVar("T")


def return_list(fn: Callable[P, Iterable[T]]) -> Callable[P, list[T]]:
    def _new_fn(*args: P.args, **kwargs: P.kwargs):
        return list(fn(*args, **kwargs))
    return _new_fn


@return_list
def generate_integers(limit: int) -> Iterator[int]:
    for i in range(limit):
        yield i


integer_to_5: list[int] = generate_integers(5)


# PEP 613

# Type aliases
Nodes = set[int]
ClientStr = "DBClient"  # here type of `Client` is str

ClientAlias: TypeAlias = "DBClient"



class DBClient:
    pass


client: ClientAlias = DBClient()
