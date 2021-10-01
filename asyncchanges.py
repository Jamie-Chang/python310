import asyncio
from contextlib import aclosing, asynccontextmanager, nullcontext
from typing import AsyncIterable, Iterable, TypeVar


T = TypeVar("T")


# aiter and anext


def first(i: Iterable[T]) -> T:
    return next(iter(i))


async def afirst(i: AsyncIterable[T]) -> T:
    return await anext(aiter(i))


# aclosing


class Connection:
    async def aclose(self) -> None:
        ...


async def connect():
    async with nullcontext():
        ...

    async with aclosing(Connection()) as connection:
        ...


# AsyncContextDecorator


@asynccontextmanager
async def nap():
    print("Hello")
    await asyncio.sleep(1)
    yield


@nap()
async def do_stuff():
    print("stuff")
