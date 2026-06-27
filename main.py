"""
main.py

Edge Cases in Scoring — Missing and Partial Signals

This file demonstrates different edge cases:
1. Worked Example
2. All Valid
3. All Missing
4. All Zero
5. Missing Video
"""

from risk_scoring_engine import RiskScoringEngine

engine = RiskScoringEngine()

# -----------------------------------------
# Test Cases
# -----------------------------------------

test_cases = [

    (
        "Worked Example (audio=None, video=150, text=70)",
        {
            "audio": None,
            "video": 150,
            "text": 70
        }
    ),

    (
        "All Valid Signals",
        {
            "audio": 80,
            "video": 70,
            "text": 90
        }
    ),

    (
        "All Missing Signals",
        {

        }
    ),

    (
        "All Zero Inputs",
        {
            "audio": 0,
            "video": 0,
            "text": 0
        }
    ),

    (
        "Missing Video Signal",
        {
            "audio": 90,
            "text": 80
        }
    )

]

# -----------------------------------------
# Execute Test Cases
# -----------------------------------------

for title, signals in test_cases:

    print("\n")
    print("=" * 60)
    print(title)
    print("=" * 60)

    try:

        result = engine.calculate_score(
            signals,
            strategy="exclude_reweight"
        )

        result.print_result()

        print("\nDictionary Output")
        print(result.to_dict())

    except Exception as e:

        print("Error:", e)