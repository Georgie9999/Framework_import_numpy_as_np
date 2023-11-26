import logging


class Logger:
    def __init__(self, name_log_file):
        self.name_log_file = name_log_file

    def setup_logging(self):
        logging.basicConfig(filename=self.name_log_file, level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        logger_var = logging.getLogger(__name__)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        logger_var.addHandler(console_handler)

        return logger_var
    
if __name__ == '__main__':
    temp = Logger('console.log')
    logger = temp.setup_logging()
    print(logger)