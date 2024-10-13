import unittest

import pandas as pd

from src.data.biannual_report_downloader import BiannualReportDownloader
from src.utils.directory_helper import DirectoryHelper


class TestBiannualReportDownloader(unittest.TestCase):

    def setUp(self):
        self._report_downloader: BiannualReportDownloader = BiannualReportDownloader()

    def test_download(self):
        try:
            csv_filepath: str = f"{DirectoryHelper().root_dir}/storage/biannual_cot_report.csv"
            result: pd.DataFrame = self._report_downloader.download(csv_filepath)

            result_length: int = len(result)
            self.assertNotEqual(0, result_length, "COT report is empty.")
            self.assertLessEqual(48, result_length, "COT report is less than 1 year.")
        except Exception as e:
            self.fail(f"Failed download test: {e}")