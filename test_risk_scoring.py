"""
test_risk_scoring.py

Unit tests for Risk Scoring Engine.
"""

import unittest

from risk_scoring_engine import RiskScoringEngine


class TestRiskScoring(unittest.TestCase):

    def setUp(self):
        """
        Create a RiskScoringEngine object before each test.
        """
        self.engine = RiskScoringEngine()

    # --------------------------------------------
    # Test Case 1: All Valid Signals
    # --------------------------------------------
    def test_all_valid(self):

        signals = {
            "audio": 80,
            "video": 70,
            "text": 90
        }

        result = self.engine.calculate_score(signals)

        self.assertEqual(result.status, "COMPLETE")
        self.assertAlmostEqual(result.score, 78.0)
        self.assertEqual(result.confidence, "HIGH")

    # --------------------------------------------
    # Test Case 2: Null Value
    # --------------------------------------------
    def test_null_value(self):

        signals = {
            "audio": None,
            "video": 80,
            "text": 70
        }

        result = self.engine.calculate_score(signals)

        self.assertEqual(result.status, "PARTIAL")
        self.assertEqual(result.confidence, "MEDIUM")

    # --------------------------------------------
    # Test Case 3: Out of Range
    # --------------------------------------------
    def test_out_of_range(self):

        signals = {
            "audio": 90,
            "video": 150,
            "text": 80
        }

        result = self.engine.calculate_score(signals)

        self.assertEqual(result.status, "PARTIAL")
        self.assertEqual(result.confidence, "MEDIUM")

    # --------------------------------------------
    # Test Case 4: All Missing
    # --------------------------------------------
    def test_all_missing(self):

        signals = {}

        result = self.engine.calculate_score(signals)

        self.assertEqual(result.status, "INCOMPLETE")
        self.assertEqual(result.score, 0)
        self.assertEqual(result.confidence, "LOW")

    # --------------------------------------------
    # Test Case 5: All Zero Inputs
    # --------------------------------------------
    def test_all_zero(self):

        signals = {
            "audio": 0,
            "video": 0,
            "text": 0
        }

        result = self.engine.calculate_score(signals)

        self.assertEqual(result.score, 0)
        self.assertEqual(result.status, "PARTIAL")

    # --------------------------------------------
    # Test Case 6: Missing Video
    # --------------------------------------------
    def test_missing_video(self):

        signals = {
            "audio": 90,
            "text": 80
        }

        result = self.engine.calculate_score(signals)

        self.assertEqual(result.status, "PARTIAL")
        self.assertAlmostEqual(result.score, 86.67, places=2)


if __name__ == "__main__":
    unittest.main()