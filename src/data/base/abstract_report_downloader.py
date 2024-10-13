from datetime import datetime, timedelta
import os.path
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

    @staticmethod
    def _from_storage(csv_filepath: str) -> pd.DataFrame | None:
        """
        Returns a locally stored CTFT COT reports if it exists.
        :param csv_filepath:
        :return:
        """
        if os.path.exists(csv_filepath):
            reports: pd.DataFrame = pd.read_csv(csv_filepath)
            reports = AbstractReportDownloader._sort_reports(reports)
            last_report_date_str: str = reports.tail(1)["As of Date in Form YYYY-MM-DD"].astype(str).values[0]
            last_report_date: datetime = datetime.strptime(last_report_date_str, "%Y-%m-%d") + timedelta(0)
            is_10days_or_more: bool = datetime.today().date() >= last_report_date.date() + timedelta(10)
            is_3_30pm_est_or_more: bool = datetime.now().time() >= datetime.strptime("15:30:00", "%H:%M:%S").time()
            if (is_10days_or_more and is_3_30pm_est_or_more) or is_10days_or_more:
                return
            return reports
        return

    @staticmethod
    def _sort_reports(reports: pd.DataFrame) -> pd.DataFrame:
        reports['As of Date in Form YYYY-MM-DD'] = pd.to_datetime(reports['As of Date in Form YYYY-MM-DD'])
        return reports.sort_values(by='As of Date in Form YYYY-MM-DD')
