class Positions:

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
            "commercial_short": self._commercial_short,
            "net": self.net,
            "net_noncommercial": self.net_noncommercial,
            "net_commercial": self.net_commercial
        }

    @property
    def net(self) -> int:
        total_long: int = self.noncommercial_long + self._commercial_long
        total_short: int = self.noncommercial_short + self._noncommercial_short
        return total_long - total_short

    @property
    def net_noncommercial(self) -> int:
        return self._noncommercial_long - self._noncommercial_short

    @property
    def net_commercial(self) -> int:
        return self._commercial_long - self._commercial_short

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
        net_positions: str = f"net: {self.net}, net noncommercial: {self.net_noncommercial}, net commercial: {self.net_commercial}"
        return f"Traders Positions({noncommercial_long}, {noncommercial_short}, {commercial_long}, {commercial_short}, {net_positions})"

    def __str__(self) -> str:
        return self.__repr__()

    def __eq__(self, other: "Positions") -> bool:
        is_equal_noncommercial_long: bool = self._noncommercial_long == other.noncommercial_long
        is_equal_noncommercial_short: bool = self._noncommercial_short == other._noncommercial_short
        is_equal_commercial_long: bool = self._commercial_long == other._commercial_long
        is_equal_commercial_short: bool = self._commercial_short == other._commercial_short
        is_net_equal: bool = self.net ==  other.net
        is_net_noncommercial_equal: bool = self.net_noncommercial == other.net_noncommercial
        is_net_commercial_equal: bool = self.net_commercial == other.net_commercial
        return is_equal_noncommercial_long \
            and is_equal_noncommercial_short \
            and is_equal_commercial_long \
            and is_equal_commercial_short \
            and is_net_equal \
            and is_net_noncommercial_equal \
            and is_net_commercial_equal
