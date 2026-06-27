from edge_case_log import EdgeCaseLog
from score_result import ScoreResult
from logger import Logger


class RiskScoringEngine:

    WEIGHTS = {
        "audio": 0.4,
        "video": 0.4,
        "text": 0.2
    }

    REQUIRED_SIGNALS = ["audio", "video", "text"]

    DEFAULT_VALUES = {
        "audio": 50,
        "video": 50,
        "text": 50
    }

    def calculate_score(
            self,
            signals,
            strategy="exclude_reweight"):

        logs = []
        valid_signals = {}

        # --------------------------
        # Missing Signal
        # --------------------------

        for signal in self.REQUIRED_SIGNALS:

            if signal not in signals:

                logs.append(
                    EdgeCaseLog(
                        signal,
                        "MISSING_SIGNAL"
                    )
                )

        # --------------------------
        # Validation
        # --------------------------

        for signal, value in signals.items():

            # NULL VALUE

            if value is None:

                logs.append(
                    EdgeCaseLog(
                        signal,
                        "NULL_VALUE"
                    )
                )

                if strategy == "domain_default":

                    valid_signals[signal] = \
                        self.DEFAULT_VALUES[signal]

                continue

            # OUT OF RANGE

            if value < 0 or value > 100:

                logs.append(
                    EdgeCaseLog(
                        signal,
                        "OUT_OF_RANGE"
                    )
                )

                continue

            valid_signals[signal] = value

        # --------------------------
        # Flag Incomplete
        # --------------------------

        if len(valid_signals) == 0:

            Logger.save(logs)

            return ScoreResult(
                0,
                "INCOMPLETE",
                logs,
                "LOW"
            )

        # --------------------------
        # All Zero Inputs
        # --------------------------

        if (
            len(valid_signals) == len(self.REQUIRED_SIGNALS)
            and all(value == 0 for value in valid_signals.values())
        ):

            logs.append(
                EdgeCaseLog(
                    "SYSTEM",
                    "ALL_ZERO_INPUTS"
                )
            )
        # --------------------------
        # Exclude & Reweight
        # --------------------------

        total_weight = 0

        for signal in valid_signals:

            total_weight += self.WEIGHTS[signal]

        score = 0

        for signal, value in valid_signals.items():

            adjusted_weight = \
                self.WEIGHTS[signal] / total_weight

            score += value * adjusted_weight

        # --------------------------
        # Confidence
        # --------------------------

        if any(log.issue == "ALL_ZERO_INPUTS" for log in logs):
            confidence = "LOW"
        elif len(logs) == 0:

            confidence = "HIGH"

        elif len(logs) == 1:

            confidence = "MEDIUM"

        else:

            confidence = "LOW"

        status = \
            "COMPLETE" if len(logs) == 0 else "PARTIAL"

        Logger.save(logs)

        return ScoreResult(
            round(score, 2),
            status,
            logs,
            confidence
        )