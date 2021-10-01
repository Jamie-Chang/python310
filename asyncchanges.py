import asyncio
from contextlib import aclosing, asynccontextmanager, nullcontext
from typing import AsyncIterable, Iterable, TypeVar

T = TypeVar("T")

# aiter and anext


def first(i: Iterable[T]) -> T:
    """Get the first element of an iterable.
    """
    return next(iter(i))


async def afirst(i: AsyncIterable[T]) -> T:
    """Get the first eleemnt of an async iterable.
    """
    return await anext(aiter(i))


# aclosing


class Connection:
    async def aclose(self) -> None:
        """Async function to close the connection.
        """
        ...


async def connect():
    async with nullcontext():
        ...

    async with aclosing(Connection()) as connection:
        ...


# AsyncContextDecorator


@asynccontextmanager
async def nap():
    """Async context decorator to sleep first.
    """
    print("Taking a nap before")
    await asyncio.sleep(1)
    yield


@nap()  # Here we use it as a decorator.
async def do_stuff():
    print("stuff")
