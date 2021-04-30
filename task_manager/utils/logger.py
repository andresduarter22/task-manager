import logging


class CustomLogger(logging.Logger):
    # Custom Logger should be created when having an app taht has many modules
    # or your app uses part time modules
    open = False
    handlers = []

    def __init__(self, name, config={}):
        self.open = True
        self.level = config.get("loglevel", logging.DEBUG)
        logging.Logger.__init__(self, name, self.level)
        self.configure()

    def close(self):
        self.open = False
        for handler in self.handlers:
            handler.flush()
            handler.close()

    def configure(self):
        # create console handler and set level to debug
        ch = logging.StreamHandler()
        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # add formatter to ch
        ch.setLevel(self.level)
        ch.setFormatter(formatter)

        f_handler = logging.FileHandler('file.log')
        f_handler.setLevel(logging.DEBUG)
        formatter2 = logging.Formatter(' formatter: %(asctime)s - %(name)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(formatter2)

        self.handlers = self.handlers + [ch, f_handler]
        for handler in self.handlers:
            self.addHandler(handler)
