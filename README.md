# Edge Cases in Scoring — Missing and Partial Signals

## Objective

Build a Risk Scoring Engine that correctly handles:

- Missing Signal
- Null Value
- Out-of-Range Value
- All-Zero Inputs

---

## Handling Strategies

### 1. Exclude & Reweight

Invalid signals are removed.

Remaining weights are adjusted.

---

### 2. Domain Default

Null values use predefined default values.

Example:

audio = None

↓

audio = 50

---

### 3. Flag as Incomplete

If all signals are invalid or missing,

Return

Status = INCOMPLETE

Score = 0

---

## Worked Example

Input

audio = None

video = 150

text = 70

Processing

✔ audio → NULL_VALUE

✔ video → OUT_OF_RANGE

✔ text → VALID

Only text remains.

Weight becomes 100%.

Final Score = 70

Status = PARTIAL

Confidence = LOW

---

## How to Run

```bash
python main.py
```