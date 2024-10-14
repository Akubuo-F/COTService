from src.models.changes import Changes
from src.models.changes_in_open_interest import ChangesInOpenInterest
from src.models.changes_in_positions import ChangesInPositions
from src.models.open_interest import OpenInterest
from src.models.positions import Positions


class CotReport:

    def __init__(
            self,
            report_date: str,
            contract_name: str,
            open_interest: OpenInterest,
            positions: Positions,
            changes: Changes | None = None
    ):
        self._report_date: str = report_date
        self._contract_name: str = contract_name
        self._open_interest: OpenInterest = open_interest
        self._positions: Positions = positions
        self._changes: Changes = changes if changes else Changes(
            ChangesInOpenInterest(0, 0, 0),
            ChangesInPositions(0, 0, 0, 0)
        )

    def to_dict(self) -> dict:
        return {
            "report_date": self._report_date,
            "contract_name": self._contract_name,
            "open_interest": self._open_interest.to_dict(),
            "positions": self._positions.to_dict(),
            "changes": self._changes.to_dict()
        }

    def set_changes(self, changes: Changes):
        self._changes = changes

    @property
    def report_date(self) -> str:
        return self._report_date

    @property
    def contract_name(self) -> str:
        return self._contract_name

    @property
    def open_interest(self) -> OpenInterest:
        return self._open_interest

    @property
    def positions(self) -> Positions:
        return self._positions

    @property
    def changes(self) -> Changes:
        return self._changes

    def __repr__(self) -> str:
        report_date: str = f"report date: {self.report_date}"
        contract_name: str = f"contract name: {self._contract_name}"
        return f"COT Report({report_date}, {contract_name}, {self.open_interest}, {self._positions}, {self._changes})"

    def __str__(self) -> str:
        return self.__repr__()

    def __eq__(self, other: "CotReport") -> bool:
        is_report_date_equal: bool = self._report_date == other.report_date
        is_contract_name_equal: bool = self._contract_name == other.contract_name
        is_open_interest_equal: bool = self._open_interest == other.open_interest
        is_positions_equal: bool = self._positions == other.positions
        is_changes_equal: bool = self._changes == other.changes
        return is_report_date_equal \
            and is_contract_name_equal \
            and is_open_interest_equal \
            and is_positions_equal \
            and is_changes_equal
