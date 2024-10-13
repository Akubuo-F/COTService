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

    def download(self, csv_filepath: str | None = None) -> pd.DataFrame:
        try:
            self._logger.info("Checking for stored reports...")
            from_storage: pd.DataFrame | None = super()._from_storage(csv_filepath)
            if from_storage is not None:
                self._logger.info("COT reports fetched from storage.")
                return from_storage
            else:
                self._logger.info("No valid stored reports found, downloading new reports ...")
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
            reports: pd.DataFrame = pd.concat(downloaded_reports, ignore_index=True)
            reports.to_csv(csv_filepath) if csv_filepath else ...
            return self._from_storage(csv_filepath)
        except Exception as e:
            self._logger.info(f"Failed to download COT reports: {e}.")
            raise
