class OpenInterest:

    def __init__(
            self,
            total: int,
            speculators: int,
            hedgers: int
    ):
        self._total: int = total
        self._speculators: int = speculators
        self._hedgers: int = hedgers

    def to_dict(self) -> dict:
        return {
            "total": self._total,
            "speculators": self.speculators,
            "hedgers": self._hedgers
        }

    @property
    def total(self) -> int:
        return self._total

    @property
    def speculators(self) -> int:
        return self._speculators

    @property
    def hedgers(self) -> int:
        return self._hedgers

    def __repr__(self) -> str:
        return f"Open Interest(total: {self._total}, speculators: {self._speculators}, hedgers: {self._hedgers})"

    def __str__(self) -> str:
        return self.__repr__()

    def __eq__(self, other: "OpenInterest") -> bool:
        is_total_equal: bool = self._total == other.total
        is_speculators_equal: bool = self._speculators == other.speculators
        is_hedgers_equal: bool = self._hedgers == other.hedgers
        return is_total_equal \
            and is_speculators_equal \
            and is_hedgers_equal
