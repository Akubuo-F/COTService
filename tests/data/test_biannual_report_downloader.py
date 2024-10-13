import unittest

import pandas as pd

from src.data.biannual_report_downloader import BiannualReportDownloader


class TestBiannualReportDownloader(unittest.TestCase):

    def setUp(self):
        self._report_downloader: BiannualReportDownloader = BiannualReportDownloader()

    def test_download(self):
        try:
            result: pd.DataFrame = self._report_downloader.download()

            result_length: int = len(result)
            self.assertNotEqual(0, result_length, "COT report is empty.")
            self.assertLessEqual(48, result_length, "COT report is less than 1 year.")
        except Exception as e:
            self.fail(f"Failed download test: {e}")