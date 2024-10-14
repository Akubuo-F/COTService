from src.models.changes import Changes
from src.models.changes_in_open_interest import ChangesInOpenInterest
from src.models.changes_in_positions import ChangesInPositions
from src.models.cot_report import CotReport
from src.models.open_interest import OpenInterest
from src.models.positions import Positions


class BuilderCotReport:

    def __init__(self):
        self._report_date: str = ""
        self._contract_name: str = ""
        self._open_interest_total: int = 0
        self._noncommercial_long: int = 0
        self._noncommercial_short: int = 0
        self._commercial_long: int = 0
        self._commercial_short: int = 0
        self._change_in_open_interest: int = 0
        self._change_in_noncommercial_long: int = 0
        self._change_in_noncommercial_short: int = 0
        self._change_in_commercial_long: int = 0
        self._change_in_commercial_short: int = 0

    def build(self) -> CotReport:
        report_date: str = self._report_date
        contract_name: str = self._contract_name
        open_interest: OpenInterest = self._build_open_interest()
        positions: Positions = self._build_positions()
        changes: Changes = self._build_changes()
        return CotReport(report_date, contract_name, open_interest, positions, changes)

    def _build_changes(self) -> Changes:
        changes_in_speculators: int = sum([self._change_in_noncommercial_long, self._change_in_noncommercial_short])
        changes_in_hedgers: int = sum([self._change_in_commercial_long, self._change_in_commercial_short])
        changes_in_open_interest: ChangesInOpenInterest = ChangesInOpenInterest(
            self._open_interest_total,
            changes_in_speculators,
            changes_in_hedgers
        )
        changes_in_positions: ChangesInPositions = ChangesInPositions(
            self._change_in_noncommercial_long,
            self._change_in_noncommercial_short,
            self._change_in_commercial_long,
            self._change_in_commercial_short
        )
        return Changes(changes_in_open_interest, changes_in_positions)

    def _build_positions(self) -> Positions:
        noncommercial_long: int = self._noncommercial_long
        noncommercial_short: int = self._noncommercial_short
        commercial_long: int = self._commercial_long
        commercial_short: int = self._commercial_short
        return Positions(noncommercial_long, noncommercial_short, commercial_long, commercial_short)

    def _build_open_interest(self) -> OpenInterest:
        total: int = self._open_interest_total
        speculators: int = sum([self._noncommercial_long, self._noncommercial_short])
        hedgers: int = sum([self._commercial_long, self._commercial_short])
        return OpenInterest(total, speculators, hedgers)

    def set_report_date(self, report_date: str) -> "BuilderCotReport":
        self._report_date = report_date
        return self

    def set_contract_name(self, contract_name: str) -> "BuilderCotReport":
        self._contract_name = contract_name
        return self

    def set_open_interest_total(self, open_interest_total: int) -> "BuilderCotReport":
        self._open_interest_total = open_interest_total
        return self

    def set_noncommercial_long(self, noncommercial_long: int) -> "BuilderCotReport":
        self._noncommercial_long = noncommercial_long
        return self

    def set_noncommercial_short(self, noncommercial_short: int ) -> "BuilderCotReport":
        self._noncommercial_short = noncommercial_short
        return self

    def set_commercial_long(self, commercial_long: int) -> "BuilderCotReport":
        self._commercial_long = commercial_long
        return self

    def set_commercial_short(self, commercial_short: int) -> "BuilderCotReport":
        self._commercial_short = commercial_short
        return self

    def set_change_in_open_interest(self, change_in_open_interest: int) -> "BuilderCotReport":
        self._change_in_open_interest = change_in_open_interest
        return self

    def set_change_in_noncommercial_long(self, change_in_noncommercial_long: int) -> "BuilderCotReport":
        self._change_in_noncommercial_long = change_in_noncommercial_long
        return self

    def set_change_in_noncommercial_short(self, change_in_noncommercial_short: int) -> "BuilderCotReport":
        self._change_in_noncommercial_short = change_in_noncommercial_short
        return self

    def set_change_in_commercial_long(self, change_in_commercial_long: int) -> "BuilderCotReport":
        self._change_in_commercial_long = change_in_commercial_long
        return self

    def set_change_in_commercial_short(self, change_in_commercial_short: int) -> "BuilderCotReport":
        self._change_in_commercial_short = change_in_commercial_short
        return self
