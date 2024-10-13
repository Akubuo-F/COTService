import logging
import os


class Logger:

    def __init__(self, name: str, log_dir: str, log_level: int = logging.INFO):
        self._logger: logging.Logger = logging.getLogger(name)
        self._log_level: int = log_level
        self._configure_logger(name, log_dir)

    def _configure_logger(self, name: str, log_dir: str):
        self._logger.setLevel(self._log_level)
        formatter: logging.Formatter = logging.Formatter("'%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        file_handler: logging.FileHandler = logging.FileHandler(os.path.join(log_dir, f"{name}.log"))
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        console_handler: logging.StreamHandler = logging.StreamHandler()
        console_handler.setLevel(self._log_level)
        console_handler.setFormatter(formatter)

        self._logger.addHandler(file_handler)
        self._logger.addHandler(console_handler)

    def get_logger(self) -> logging.Logger:
        return self._logger
