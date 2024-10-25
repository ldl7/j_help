
def undo_last(self):
     """
    Removes the last calculation from the history.
    """
     if self.calculations:
        self.calculations.pop()
     else:
        print("History is already empty.")
