from position import Position
from typing import Iterator
from typing_extensions import Self

class Cell:
    def __init__(self, alive: bool, position: Position) -> None:
        self.alive = alive
        self.position = position

    def get_neibourghs(self) -> Iterator[Self]:
        pass

    def die(self) -> None:
        pass

    def spawn(self) -> None:
        pass

    def apply_rules(self) -> None:
        pass

    