"""
score_result.py

Stores the final output produced by
the Risk Scoring Engine.
"""


class ScoreResult:

    def __init__(self,
                 score,
                 status,
                 logs,
                 confidence="HIGH"):
        """
        Parameters:
            score (float): Final calculated score
            status (str): COMPLETE, PARTIAL, INCOMPLETE
            logs (list): List of EdgeCaseLog objects
            confidence (str): HIGH, MEDIUM, LOW
        """

        self.score = score
        self.status = status
        self.logs = logs
        self.confidence = confidence

    def print_result(self):
        """
        Displays the final scoring result.
        """

        print("\n========== FINAL RESULT ==========")

        print(f"Status      : {self.status}")
        print(f"Score       : {self.score:.2f}")
        print(f"Confidence  : {self.confidence}")

        print("\nDetected Edge Cases:")

        if len(self.logs) == 0:
            print("No edge cases detected.")

        else:
            for log in self.logs:
                print(log)

    def to_dict(self):
        """
        Converts result into dictionary.
        Useful for APIs or JSON output.
        """

        return {

            "score": self.score,

            "status": self.status,

            "confidence": self.confidence,

            "logs": [
                log.to_dict()
                for log in self.logs
            ]

        }