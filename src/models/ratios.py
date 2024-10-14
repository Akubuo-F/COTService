class Ratios:

    def __init__(
            self,
            speculators: float,
            hedgers: float,
            noncommercial_long: float,
            noncommercial_short: float,
            commercial_long: float,
            commercial_short: float
    ):
        self._speculators: float = round(speculators, 1)
        self._hedgers: float = round(hedgers, 1)
        self._noncommercial_long: float = round(noncommercial_long, 1)
        self._noncommercial_short: float = round(noncommercial_short, 1)
        self._commercial_long: float = round(commercial_long, 1)
        self._commercial_short: float = round(commercial_short, 1)

    def to_dict(self) -> dict:
        return {
            "speculators": self._speculators,
            "hedgers": self._hedgers,
            "noncommercial_long": self._noncommercial_long,
            "noncommercial_short": self._noncommercial_short,
            "commercial_long": self._commercial_long,
            "commercial_short": self._commercial_short
        }

    @property
    def speculators(self) -> float:
        return self._speculators

    @property
    def hedgers(self) -> float:
        return self._hedgers

    @property
    def noncommercial_long(self) -> float:
        return self._noncommercial_long

    @property
    def noncommercial_short(self) -> float:
        return self._noncommercial_short

    @property
    def commercial_long(self) -> float:
        return self._commercial_long

    @property
    def commercial_short(self) -> float:
        return self._commercial_short

    def __repr__(self) -> str:
        speculators: str = f"speculators: {self._speculators}"
        hedgers: str = f"hedgers: {self._hedgers}"
        noncommercial_long: str = f"noncommercial long: {self._noncommercial_long}"
        noncommercial_short: str = f"noncommercial short: {self._noncommercial_short}"
        commercial_long: str = f"commercial long: {self._commercial_long}"
        commercial_short: str = f"commercial short: {self._commercial_short}"
        return f"Ratios({speculators}, {hedgers}, {noncommercial_long}, {noncommercial_short}, {commercial_long}, {commercial_short})"

    def __str__(self) -> str:
        return self.__repr__()

    def __eq__(self, other: "Ratios") -> bool:
        is_equal_speculators: bool = self._speculators == other.speculators
        is_equal_hedgers: bool = self._hedgers == other.hedgers
        is_equal_noncommercial_long: bool = self._noncommercial_long == other.noncommercial_long
        is_equal_noncommercial_short: bool = self._noncommercial_short == other.noncommercial_short
        is_equal_commercial_long: bool = self._commercial_long == other.commercial_long
        is_equal_commercial_short: bool = self._commercial_short == other.commercial_short
        return is_equal_speculators \
            and is_equal_hedgers \
            and is_equal_noncommercial_long \
            and is_equal_noncommercial_short \
            and is_equal_commercial_long \
            and is_equal_commercial_short
