import datetime
import os

class Logger:
    """"Save erros in a file for future analysis of logs to improve the system and debug"""
    def __init__(self, log_path: str):
        self.log_path = log_path
        self._create_log_file()

    def _create_log_file(self):
        log_dir = os.path.dirname(self.log_path)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        if not os.path.exists(self.log_path):
            with open(self.log_path, 'w') as f:
                f.write("")

    def log_failure(self, error: Exception):
        with open(self.log_path, 'a') as f:
            f.write(f'{datetime.datetime.now()} - Failure: {str(error)}\n')