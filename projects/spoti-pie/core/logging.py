import argparse
import logging

class Logger():
    
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--log",
            "--log-level",
            default="warning",
            help=(
                "Provide logging level."
                "Example --log-level debug, default='warning'"
            )
        )
        options = parser.parse_args()
        levels = {
            'critical': logging.CRITICAL,
            'error': logging.ERROR,
            'warn': logging.WARNING,
            'warning': logging.WARNING,
            'info': logging.INFO,
            'debug': logging.DEBUG
        }
        level = levels.get(options.log.lower())
        if level is None:
            raise ValueError(
                f"log level given: {options.log}"
                f" -- must be one of: {' | '.join(levels.keys())}")
        self.logger = logging.getLogger("spotipie")
        self.logger.setLevel(level)
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(level)
        formatter = logging.Formatter('%(asctime)s [%(name)s] [%(levelname)s]: %(message)s', datefmt='%m/%d/%Y %I:%M:%S%p')
        consoleHandler.setFormatter(formatter)
        self.logger.addHandler(consoleHandler)