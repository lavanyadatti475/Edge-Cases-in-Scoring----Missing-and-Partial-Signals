# Edge Cases in Scoring — Missing and Partial Signals

# Project Overview

This project implements a **Risk Scoring Engine** that calculates a final score using three input signals:

* Audio Score
* Video Score
* Text Score

Before calculating the final score, the system validates every signal and detects different edge cases that may affect the reliability of the result.

Instead of silently ignoring invalid inputs, the system:

* Detects edge cases
* Applies an appropriate handling strategy
* Logs detected issues
* Calculates the score using valid signals
* Returns a clear status and confidence level

---

# Objectives

The project demonstrates how to:

* Detect missing signals
* Handle null values
* Validate score ranges
* Detect all-zero inputs
* Apply different handling strategies
* Log edge cases for future review
* Return meaningful scoring results

---

# Edge Cases Covered

| Edge Case          | Description                              | Handling Strategy         | Returned Status      |
| ------------------ | ---------------------------------------- | ------------------------- | -------------------- |
| Missing Signal     | Required signal is not collected         | Exclude & Reweight        | PARTIAL / INCOMPLETE |
| Null Value         | Signal collected but value is empty      | Exclude or Domain Default | PARTIAL              |
| Out-of-Range Value | Value is outside the valid range (0–100) | Exclude & Reweight        | PARTIAL              |
| All-Zero Inputs    | All signal values are zero               | Log warning               | PARTIAL              |

---

# Handling Strategies

## 1. Exclude & Reweight

Invalid signals are excluded from scoring.

The remaining valid signals are assigned adjusted weights before calculating the final score.

Example:

Original weights

* Audio = 40%
* Video = 40%
* Text = 20%

If Audio and Video become invalid:

* Text = 100%

---

## 2. Domain Default

Instead of excluding a null value, the system can replace it with a predefined default value.

Example:

```text
Audio = None

↓

Audio = 50
```

---

## 3. Flag as Incomplete

If all required signals are missing or invalid, the system returns:

```text
Status = INCOMPLETE

Score = 0
```

instead of producing an unreliable score.

---

# Project Structure

```text
Task9_EdgeCases/

│── signal.py
│── edge_case_log.py
│── score_result.py
│── logger.py
│── risk_scoring_engine.py
│── main.py
│── test_risk_scoring.py
│── edgecase_log.txt
└── README.md
```

---

# Workflow

```text
Input Signals
      │
      ▼
Signal Validation
      │
      ▼
Detect Edge Cases
      │
      ▼
Apply Handling Strategy
      │
      ▼
Recalculate Weights
      │
      ▼
Calculate Final Score
      │
      ▼
Generate Result
      │
      ▼
Save Edge Case Logs
```

---

# Worked Example

### Input

```python
signals = {

    "audio": None,

    "video": 150,

    "text": 70

}
```

### Processing

* Audio is detected as **NULL_VALUE**
* Video is detected as **OUT_OF_RANGE**
* Text is valid

Only the text signal is used.

After reweighting:

```text
Text Weight = 100%
```

Final Score:

```text
70
```

---

# Sample Output

```text
========== FINAL RESULT ==========

Status      : PARTIAL
Score       : 70.00
Confidence  : LOW

Detected Edge Cases:

audio --> NULL_VALUE
video --> OUT_OF_RANGE
```

---

# Test Cases

The following test cases are implemented:

### 1. Worked Example

Input:

```text
Audio = None

Video = 150

Text = 70
```

Expected Status:

```text
PARTIAL
```

---

### 2. All Valid Signals

Input:

```text
Audio = 80

Video = 70

Text = 90
```

Expected Status:

```text
COMPLETE
```

---

### 3. All Missing Signals

Input:

```text
{}
```

Expected Status:

```text
INCOMPLETE
```

---

### 4. All Zero Inputs

Input:

```text
Audio = 0

Video = 0

Text = 0
```

Expected Status:

```text
PARTIAL
```

---

### 5. Missing Video Signal

Input:

```text
Audio = 90

Text = 80
```

Expected Status:

```text
PARTIAL
```

---

# Logging

Every detected edge case is saved to:

```text
edgecase_log.txt
```

Example:

```text
audio --> NULL_VALUE

video --> OUT_OF_RANGE
```

Logging helps developers review and debug data quality issues.

---

# Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* File Handling
* Exception Handling
* Dictionaries
* Unit Testing (unittest)

---

# How to Run

Run the main program:

```bash
python main.py
```

Run unit tests:

```bash
python -m unittest test_risk_scoring.py
```

---

# Expected Output

The program demonstrates:

* Worked Example
* All Valid Signals
* All Missing Signals
* All Zero Inputs
* Missing Video Signal

Each test case displays:

* Final Score
* Status
* Confidence
* Detected Edge Cases
* Dictionary Output

---

# Learning Outcomes

This project demonstrates:

* Input Validation
* Edge Case Detection
* Risk Score Calculation
* Score Reweighting
* Logging
* Decision Engine Design
* Transparent Error Handling
* Modular Python Programming

---

# Conclusion

This project successfully implements a Risk Scoring Engine capable of handling incomplete and invalid input signals. It detects edge cases, applies appropriate handling strategies, logs detected issues, and generates reliable scoring results. By explicitly surfacing data quality problems instead of hiding them, the system provides more transparent, explainable, and trustworthy decision-making.

---


**Task 9 – Edge Cases in Scoring: Missing and Partial Signals**
