from enum import Enum
from typing import Callable
from dataclasses import dataclass
from coordinates import MoveVector


class EndLine(Enum):
    TOP = MoveVector(x=1, y=1)
    BOTTOM = MoveVector(x=1, y=-1)


@dataclass
class Player:
    direction: EndLine
    symbol_transformation: Callable[[str], str]
