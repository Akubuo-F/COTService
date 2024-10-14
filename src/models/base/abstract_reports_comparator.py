from abc import ABC, abstractmethod

from src.models.changes_in_open_interest import ChangesInOpenInterest
from src.models.changes_in_positions import ChangesInPositions


class AbstractReportsComparator(ABC):

    @staticmethod
    @abstractmethod
    def get_changes_in_open_interest() -> ChangesInOpenInterest:
        ...

    @staticmethod
    @abstractmethod
    def get_changes_in_positions() -> ChangesInPositions:
        ...