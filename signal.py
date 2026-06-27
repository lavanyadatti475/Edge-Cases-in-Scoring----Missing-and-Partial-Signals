"""
signal.py

Represents a signal used in the Risk Scoring Engine.
Each signal has:
1. name  -> Name of the signal (audio, video, text)
2. value -> Score received (0-100, None, etc.)
"""


class Signal:
    """
    Represents a single scoring signal.
    """

    def __init__(self, name, value):
        """
        Initialize a Signal object.

        Parameters:
            name (str): Name of the signal.
            value (float or None): Score of the signal.
        """
        self.name = name
        self.value = value

    def is_missing(self):
        """
        Returns False because if a Signal object exists,
        it has been collected.
        Missing signals are detected by checking whether
        the signal exists in the input dictionary.
        """
        return False

    def is_null(self):
        """
        Returns True if the signal value is None.
        """
        return self.value is None

    def is_out_of_range(self):
        """
        Returns True if the signal value is outside 0-100.
        """
        if self.value is None:
            return False

        return self.value < 0 or self.value > 100

    def is_zero(self):
        """
        Returns True if the signal value is exactly 0.
        """
        return self.value == 0

    def __str__(self):
        """
        String representation of the Signal object.
        """
        return f"{self.name}: {self.value}"