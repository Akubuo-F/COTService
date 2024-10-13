from abc import ABC, abstractmethod
from typing import Final

import pandas as pd


class AbstractReportDownloader(ABC):
    LEGACY_REPORT_FUTURES_ONLY: Final[str] = "legacy_fut"

    @abstractmethod
    def download(self, csv_filepath: str) -> pd.DataFrame:
        """
        Downloads CTFT COT reports.
        :param csv_filepath: (str) csv file to save the downloaded CTFT COT reports.
        :return: pd.DataFrame
        """
        ...