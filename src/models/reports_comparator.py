from src.models.base.abstract_reports_comparator import AbstractReportsComparator
from src.models.changes_in_open_interest import ChangesInOpenInterest
from src.models.changes_in_positions import ChangesInPositions
from src.models.cot_report import CotReport


class ReportsComparator(AbstractReportsComparator):

    def __init__(self):
        self._recent: CotReport | None = None
        self._previous: CotReport | None = None

    def set_recent_and_previous_reports(self, recent: CotReport, previous: CotReport):
        self._recent = recent
        self._previous = previous

    def get_changes_in_open_interest(self) -> ChangesInOpenInterest:
        recent_total: int = self._recent.open_interest.total
        previous_total: int = self._recent.open_interest.total
        changes_in_total: int = recent_total - previous_total

        recent_speculators: int = self._recent.positions.noncommercial_long + self._recent.positions.noncommercial_short
        previous_speculators: int = self._previous.positions.noncommercial_long + self._previous.positions.noncommercial_short
        changes_in_speculators: int = recent_speculators - previous_speculators

        recent_hedgers: int = self._recent.positions.commercial_long + self._recent.positions.commercial_short
        previous_hedgers: int = self._previous.positions.commercial_long + self._previous.positions.commercial_short
        changes_in_hedgers: int = recent_hedgers - previous_hedgers
        return ChangesInOpenInterest(changes_in_total, changes_in_speculators, changes_in_hedgers)

    def get_changes_in_positions(self) -> ChangesInPositions:
        recent_noncommercial_long: int = self._recent.positions.noncommercial_long
        previous_noncommercial_long: int = self._previous.positions.noncommercial_long
        changes_in_noncommercial_long: int = recent_noncommercial_long - previous_noncommercial_long

        recent_noncommercial_short: int = self._recent.positions.noncommercial_short
        previous_noncommercial_short: int = self._previous.positions.noncommercial_short
        changes_in_noncommercial_short: int = recent_noncommercial_short - previous_noncommercial_short

        recent_commercial_long: int = self._recent.positions.commercial_long
        previous_commercial_long: int = self._previous.positions.commercial_long
        changes_in_commercial_long: int = recent_commercial_long - previous_commercial_long

        recent_commercial_short: int = self._recent.positions.commercial_short
        previous_commercial_short: int = self._previous.positions.commercial_short
        changes_in_commercial_short: int = recent_commercial_short - previous_commercial_short
        return ChangesInPositions(
            changes_in_noncommercial_long,
            changes_in_noncommercial_short,
            changes_in_commercial_long,
            changes_in_commercial_short
        )