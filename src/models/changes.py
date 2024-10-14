from src.models.changes_in_open_interest import ChangesInOpenInterest
from src.models.changes_in_positions import ChangesInPositions


class Changes:
    def __init__(
            self,
            open_interest: ChangesInOpenInterest,
            traders_positions: ChangesInPositions,

    ):
        self._open_interest: ChangesInOpenInterest = open_interest
        self._traders_positions: ChangesInPositions = traders_positions

    def to_dict(self) -> dict:
        return {
            "open_interest": self._open_interest.to_dict(),
            "traders_positions": self._traders_positions.to_dict()
        }

    @property
    def open_interest(self) -> ChangesInOpenInterest:
        return self._open_interest

    @property
    def traders_positions(self) -> ChangesInPositions:
        return self._traders_positions

    def __repr__(self) -> str:
        return f"Changes(open interest: {self._open_interest}, traders positions: {self._traders_positions}"

    def __str__(self) -> str:
        return self.__repr__()

    def __eq__(self, other: "Changes") -> bool:
        is_open_interest_equal: bool = self._open_interest == other.open_interest
        is_traders_positions_equal: bool = self._traders_positions == other.traders_positions
        return is_open_interest_equal \
            and is_traders_positions_equal
