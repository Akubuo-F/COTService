import os


class DirectoryHelper:

    @staticmethod
    def root_dir() -> str:
        """
        This method assumes the root directory contains a unique identifier src folder,
        which will act as a unique identifier for the r
        :return: str
        """
        current_dir: str = os.path.dirname(os.path.abspath(__file__))
        while current_dir != os.path.dirname(current_dir):
            if os.path.exists(os.path.join(current_dir, "src")):
                return current_dir
            current_dir = os.path.dirname(current_dir)
        raise FileNotFoundError("Root directory containing 'config' not found.")

    @staticmethod
    def log_dir() -> str:
        return f"{DirectoryHelper.root_dir()}/logs"

if __name__ == '__main__':
    print(DirectoryHelper().root_dir)