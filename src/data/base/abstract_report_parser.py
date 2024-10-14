from abc import ABC, abstractmethod

import pandas as pd

from src.models.cot_report import CotReport


class AbstractReportParser(ABC):

    @abstractmethod
    def parse(self, data: pd.DataFrame) -> list[CotReport]:
        ...