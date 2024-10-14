class ChangesInPositions:

    def __init__(
            self,
            noncommercial_long: int,
            noncommercial_short: int,
            commercial_long: int,
            commercial_short: int
    ):
        self._noncommercial_long: int = noncommercial_long
        self._noncommercial_short: int = noncommercial_short
        self._commercial_long: int = commercial_long
        self._commercial_short: int = commercial_short

    def to_dict(self) -> dict:
        return {
            "noncommercial_long": self._noncommercial_long,
            "noncommercial_short": self._noncommercial_short,
            "commercial_long": self._commercial_long,
            "commercial_short": self._commercial_short
        }

    @property
    def noncommercial_long(self) -> int:
        return self._noncommercial_long

    @property
    def noncommercial_short(self) -> int:
        return self._noncommercial_short

    @property
    def commercial_long(self) -> int:
        return self._commercial_long

    @property
    def commercial_short(self) -> int:
        return self._commercial_short

    def __repr__(self) -> str:
        noncommercial_long: str = f"noncommercial long: {self._noncommercial_long}"
        noncommercial_short: str = f"noncommercial short: {self._noncommercial_short}"
        commercial_long: str = f"commercial long: {self._commercial_long}"
        commercial_short: str = f"commercial short: {self._commercial_short}"
        return f"Changes In Traders Positions({noncommercial_long}, {noncommercial_short}, {commercial_long}, {commercial_short})"

    def __str__(self) -> str:
        return self.__repr__()

    def __eq__(self, other: "ChangesInPositions") -> bool:
        is_noncommercial_long_equal: bool = self._noncommercial_long == other.noncommercial_long
        is_noncommercial_short_equal: bool = self._noncommercial_short == other.noncommercial_short
        is_commercial_long_equal: bool = self._commercial_long == other._commercial_long
        is_commercial_short_equal: bool = self._commercial_short == other.commercial_short
        return is_noncommercial_long_equal \
            and is_noncommercial_short_equal \
            and is_commercial_long_equal \
            and is_commercial_short_equal
