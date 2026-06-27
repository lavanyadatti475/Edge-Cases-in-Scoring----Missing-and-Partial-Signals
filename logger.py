"""
logger.py

Saves edge case logs into a text file.
"""

from datetime import datetime


class Logger:

    FILE_NAME = "edgecase_log.txt"

    @staticmethod
    def save(logs):

        with open(Logger.FILE_NAME, "a") as file:

            file.write("\n")
            file.write("=" * 50 + "\n")
            file.write(f"Date : {datetime.now()}\n")

            if len(logs) == 0:
                file.write("No Edge Cases\n")

            else:
                for log in logs:
                    file.write(str(log) + "\n")