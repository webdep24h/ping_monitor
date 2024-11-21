import logging
import os
from datetime import datetime

class Logger:
    def __init__(self, log_file):
        self.log_file = log_file
        self._setup_logger()

    def _setup_logger(self):
        # Tạo thư mục logs nếu chưa tồn tại
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)

        # Cấu hình logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.log_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def warning(self, message):
        self.logger.warning(message)

    def get_logs(self, lines=100):
        if not os.path.exists(self.log_file):
            return []
        with open(self.log_file, 'r') as f:
            return f.readlines()[-lines:]