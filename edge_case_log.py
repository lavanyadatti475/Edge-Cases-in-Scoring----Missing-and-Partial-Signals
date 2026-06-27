
class EdgeCaseLog:
    
    def __init__(self, signal_name, issue):
        """
        Parameters:
            signal_name (str): Name of the signal
            issue (str): Type of edge case
        """
        self.signal_name = signal_name
        self.issue = issue

    def __str__(self):
        """
        Returns a readable string for printing or logging.
        """
        return f"{self.signal_name} --> {self.issue}"

    def to_dict(self):
        """
        Returns log information as a dictionary.
        Useful if saving logs in JSON format.
        """
        return {
            "signal": self.signal_name,
            "issue": self.issue
        }