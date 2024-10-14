import logging
from typing import Final

import pandas as pd

from src.data.base.abstract_report_parser import AbstractReportParser
from src.models.builder_cot_report import BuilderCotReport
from src.models.changes import Changes
from src.models.changes_in_open_interest import ChangesInOpenInterest
from src.models.changes_in_positions import ChangesInPositions
from src.models.cot_report import CotReport
from src.models.reports_comparator import ReportsComparator
from src.utils.directory_helper import DirectoryHelper
from src.utils.logger import Logger


class ReportParser(AbstractReportParser):
    REQUIRED_COLUMNS: Final[list[str]] = [
        "As of Date in Form YYYY-MM-DD",
        "Market and Exchange Names",
        "Open Interest (All)",
        "Noncommercial Positions-Long (All)",
        "Noncommercial Positions-Short (All)",
        "Commercial Positions-Long (All)",
        "Commercial Positions-Short (All)",
        "Change in Open Interest (All)",
        "Change in Noncommercial-Long (All)",
        "Change in Noncommercial-Short (All)",
        "Change in Commercial-Long (All)",
        "Change in Commercial-Short (All)"
    ]

    def __init__(self):
        self._logger: logging.Logger = Logger(__name__, DirectoryHelper.log_dir()).get_logger()
        self._report_builder: BuilderCotReport = BuilderCotReport()
        self._reports_comparator: ReportsComparator = ReportsComparator()

    def parse(self, data: pd.DataFrame) -> list[CotReport]:
        # needs at least two reports in data so that changes can be computed.
        if len(data) < 2:
            self._logger.error("Can't parse data, must have at least 2 reports in data.")
            raise ValueError("Can't parse data, must have at least 2 reports in data.")
        self._validate_data(data)
        cot_reports: list[CotReport] = []
        for i in range(-1, -len(data), -1):
            recent_report = self._make_cot_report(data.iloc[i])
            previous_report = self._make_cot_report(data.iloc[i - 1])
            self._reports_comparator.set_recent_and_previous_reports(recent_report, previous_report)
            changes_in_open_interest: ChangesInOpenInterest = self._reports_comparator.get_changes_in_open_interest()
            changes_in_positions: ChangesInPositions = self._reports_comparator.get_changes_in_positions()
            changes: Changes = Changes(changes_in_open_interest, changes_in_positions)
            recent_report.set_changes(changes)
            cot_reports.insert(0, recent_report)

            # only inserts the previous report if at the last iteration
            # this ensures that all reports in the data are actually parsed.
            if i == -len(data) + 1:
                cot_reports.insert(0, previous_report)
        return cot_reports

    def _make_cot_report(self, row: pd.Series) -> CotReport:
        columns: list[str] = ReportParser.REQUIRED_COLUMNS
        self._report_builder: BuilderCotReport = BuilderCotReport()
        self._report_builder.set_report_date(row[columns[0]])
        self._report_builder.set_contract_name(row[columns[1]])
        self._report_builder.set_open_interest_total(row[columns[2]])
        self._report_builder.set_noncommercial_long(row[columns[3]])
        self._report_builder.set_noncommercial_short(row[columns[4]])
        self._report_builder.set_commercial_long(row[columns[5]])
        self._report_builder.set_commercial_short(row[columns[6]])
        self._report_builder.set_change_in_open_interest(row[columns[7]])
        self._report_builder.set_change_in_noncommercial_long(int(row[columns[8]]))
        self._report_builder.set_change_in_noncommercial_short(int(row[columns[9]]))
        self._report_builder.set_change_in_commercial_long(int(row[columns[10]]))
        self._report_builder.set_change_in_commercial_short(int(row[columns[11]]))
        return self._report_builder.build()

    def _validate_data(self, data: pd.DataFrame) -> None:
        data_columns: pd.Index = data.columns
        for column in ReportParser.REQUIRED_COLUMNS:
            if column not in data_columns:
                self._logger.error(f"Can't find '{column}' as a column in data.")
                raise LookupError(f"Can't find '{column}' as a column in data.")