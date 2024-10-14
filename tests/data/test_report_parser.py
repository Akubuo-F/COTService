import unittest

import pandas as pd

from src.data.base.abstract_report_downloader import AbstractReportDownloader
from src.data.biannual_report_downloader import BiannualReportDownloader
from src.data.report_parser import ReportParser
from src.models.changes import Changes
from src.models.changes_in_open_interest import ChangesInOpenInterest
from src.models.changes_in_positions import ChangesInPositions
from src.models.cot_report import CotReport
from src.models.open_interest import OpenInterest
from src.models.positions import Positions
from src.utils.directory_helper import DirectoryHelper


class TestReportParser(unittest.TestCase):

    def setUp(self):
        self._report_parser: ReportParser = ReportParser()

    def test_parse(self):
        try:
            report_downloader: AbstractReportDownloader = BiannualReportDownloader()
            reports: pd.DataFrame = report_downloader.download(
                f"{DirectoryHelper.root_dir()}/storage/biannual_cot_report.csv"
            ).tail(2)

            expected: CotReport = CotReport(
                report_date="2024-10-08",
                contract_name="WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE",
                open_interest=OpenInterest(total=1707072, speculators=417009, hedgers=1615417),
                positions=Positions(noncommercial_long=303823, noncommercial_short=113186, commercial_long=700799,
                                    commercial_short=914618),
                changes=Changes(
                    open_interest=ChangesInOpenInterest(total= -64264, speculators=-13171, hedgers=-5113),
                    traders_positions=ChangesInPositions(
                        noncommercial_long=8929,
                        noncommercial_short=-22100,
                        commercial_long=-22164,
                        commercial_short=17051
                    )
                )
            )

            result: CotReport = self._report_parser.parse(reports)[-1]
            compare_reports(expected, result)
            self.assertEqual(expected, result, "Result is different from Expected.")
        except Exception as e:
            self.fail(f"Test Failed: {e}.")


# Helper function to visualise what values matched or didn't
def compare_reports(expected: CotReport, result: CotReport) -> None:
    comparisons = [
        ("report_date", expected.report_date, result.report_date),
        ("contract_name", expected.contract_name, result.contract_name),
        ("open_interest_total", expected.open_interest.total, result.open_interest.total),
        ("open_interest_speculators", expected.open_interest.speculators, result.open_interest.speculators),
        ("open_interest_hedgers", expected.open_interest.hedgers, result.open_interest.hedgers),
        ("noncommercial_long", expected.positions.noncommercial_long, result.positions.noncommercial_long),
        ("noncommercial_short", expected.positions.noncommercial_short, result.positions.noncommercial_short),
        ("commercial_long", expected.positions.commercial_long, result.positions.commercial_long),
        ("commercial_short", expected.positions.commercial_short, result.positions.commercial_short),
        ("change_in_open_interest_speculators", expected.changes.open_interest.speculators, result.changes.open_interest.speculators),
        ("change_in_open_interest_hedgers", expected.changes.open_interest.hedgers, result.changes.open_interest.hedgers),
        ("change_in_noncommercial_long", expected.changes.traders_positions.noncommercial_long, result.changes.traders_positions.noncommercial_long),
        ("change_in_noncommercial_short", expected.changes.traders_positions.noncommercial_short, result.changes.traders_positions.noncommercial_short),
        ("change_in_commercial_long", expected.changes.traders_positions.commercial_long, result.changes.traders_positions.commercial_long),
        ("change_in_commercial_short", expected.changes.traders_positions.commercial_short, result.changes.traders_positions.commercial_short),
    ]
    print("\n---Matches and Misses---\n")
    for field, expected_value, result_value in comparisons:
        if expected_value != result_value:
            print(f"Mismatch in {field}: expected {expected_value}, got {result_value}")
        else:
            print(f"{field} matches.")


if __name__ == '__main__':
    unittest.main()
