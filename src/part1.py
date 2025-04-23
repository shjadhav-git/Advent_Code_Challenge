# src/part1.py

class TrebuchetPart1:
    def calculate(self, lines):
        """
        Extracts the first and last digit from each line containing numeric characters.
        Combines them into a 2-digit number and returns the total sum across all lines.
        """
        total_sum = 0
        for line in lines:
            digits = [char for char in line if char.isdigit()]  # Extract all digit characters from the line
            if digits:
                number = int(digits[0] + digits[-1])    # Combine the first and last digit
                total_sum += number     # Add the 2-digit number to total
        return total_sum