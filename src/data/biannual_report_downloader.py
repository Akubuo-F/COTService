import datetime
import logging

import cot_reports
import pandas as pd

from src.data.base.abstract_report_downloader import AbstractReportDownloader
from src.utils.directory_helper import DirectoryHelper
from src.utils.logger import Logger


class BiannualReportDownloader(AbstractReportDownloader):

    def __init__(self):
        self._logger: logging.Logger = Logger(__name__, DirectoryHelper().log_dir).get_logger()

    def download(self) -> pd.DataFrame:
        try:
            current_year: int = datetime.datetime.now().year
            previous_year: int = current_year - 1
            downloaded_reports: list[pd.DataFrame] = []
            for year in (previous_year, current_year):
                report: pd.DataFrame = cot_reports.cot_year(
                    year,
                    cot_report_type=super().LEGACY_REPORT_FUTURES_ONLY,
                    verbose=False,
                    store_txt=False
                )
                downloaded_reports.append(report)
            self._logger.info("COT reports downloaded successfully.")
            return pd.concat(downloaded_reports, ignore_index=True)
        except Exception as e:
            self._logger.info(f"Failed to download COT reports: {e}.")
            raise