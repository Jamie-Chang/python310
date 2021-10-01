from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


def locate(point: Point) -> None:
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"On the y axis {y = }")
        case Point(x=x, y=0):
            print(f"On the x axis {x = }")
        case Point(x, y) if x == y and x > 0:
            print(f"North East")
        case Point(x, y) if x == -y and x > 0:
            print("South East")
        case Point():
            print("Some other place")
        case _:
            print("Not a point")


def unpack_points(scores: list) -> None:
    match scores:
        case []:
            print("No players")
        case [None, None]:
            print("No scores")
        case [score1, score2]:
            print(f"Score {score1} - {score2}")
        case [[s1, g1, p1], [s2, g2, p2]]:
            print(f"Set-game-point: ({s1}-{s2}), ({g1}-{g2}), ({p1}-{p2})")
        case [first_score, *_]:
            print(f"First score is {first_score}")


def unpack_dict(point: dict) -> None:
    match point:
        case {"x": 0, "y": 0}:
            print("Origin")
        case {"x": 0, "y": y}:
            print(f"On the y axis {y = }")
        case {"x": x, "y": 0}:
            print(f"On the x axis {x = }")
        case {"x": x, "y": y} if x == y and x > 0:
            print(f"North East")
        case {"x": x, "y": y} if x == -y and x > 0:
            print("South East")
        case {**__}:
            print("Some other place")
        case _:
            print("Not a point")


locate(Point(0, 0))
locate(Point(0, 1))
locate(Point(1, 1))


unpack_points([None, None])
unpack_points([1, None, None])


unpack_dict({'x': 1, 'y': -1})
