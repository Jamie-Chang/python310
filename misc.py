from contextlib import ExitStack
from itertools import zip_longest

# Context managers
# 5 ways to have nested context managers.
# 4th method is added in 3.10.


with open("typehints.py") as foo, open("typehints.py") as bar:
    pass


with open("typehints.py") as foo:
    with open("typehints.py") as bar:
        pass


with open("typehints.py") as foo,\
    open("typehints.py") as bar:
    pass


with (
    open("typehints.py") as foo,
    open("typehints.py") as bar,
):
    pass


with ExitStack() as s:
    foo = s.enter_context(open("typehints.py"))
    bar = s.enter_context(open("typehints.py"))


# PEP 618
print(list(zip([1, 2], ["a"])))
print(list(zip_longest([1, 2], ["a"], fillvalue="")))
# print(list(zip([1, 2], ["a"], strict=True)))  # type: ignore -- pylance doesn't like it right now



# Dataclasses
from dataclasses import KW_ONLY, dataclass, field
from datetime import date


@dataclass(kw_only=True)
class Birthday:
    name: str = ""
    birthday: date


# Birthday("Jamie", date(1980, 1, 1))  # Fail both type check and runtime
Birthday(name="Jamie", birthday=date(1980, 1, 1))



@dataclass
class Birthday2:
    name: str
    birthday: date = field(kw_only=True)


# Marker to mark keyword only arguments
@dataclass
class Point:
    x: float
    y: float
    _: KW_ONLY  # Like the * symbol
    z: float = 0.0
    t: float = 0.0


class Record1:
    """Record class with `x` and `y` attributes in slots.

    This allows the faster attribute access and use less memory.
    """
    __slots__ = ("x", "y")  # Annoying to write

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        ...


@dataclass(slots=True)
class Record2:
    """Record class with slots using new dataclass option.
    """
    x: int
    y: int
