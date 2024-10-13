from abc import ABC, abstractmethod
from typing import Final

import pandas as pd


class AbstractReportDownloader(ABC):
    LEGACY_REPORT_FUTURES_ONLY: Final[str] = "legacy_fut"

    @abstractmethod
    def download(self) -> pd.DataFrame:
        """
        Downloads CTFT COT reports.
        :return: pd.DataFrame
        """
        ...