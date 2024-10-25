def add_calculation(self, calculation: str):
        """
        Adds a calculation to the history.
        :param calculation: String representation of the calculation.
        """
        if not isinstance(calculation, str):
            raise TypeError("Calculation must be a string.")
        self.calculations.append(calculation)
