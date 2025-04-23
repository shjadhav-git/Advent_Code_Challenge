# src/part2.py

class TrebuchetPart2:
    def __init__(self):
        # Mapping from words to their corresponding digit strings
        self.word_to_digit = {
            "one": "1", "two": "2", "three": "3", "four": "4",
            "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
        }

    def calculate(self, lines):
        """
        Extracts both numeric digits and spelled letter digits from each line.
        Converts them to digit strings, combines first and last found digits,
        and returns the total sum across all lines.
        """
        total_sum = 0
        for line in lines:
            line = line.strip()     # Remove whitespace and newline
            extracted = []      # List to store extracted digits
            for i in range(len(line)):
                if line[i].isdigit():
                    extracted.append(line[i])
                else:
                    # Check for matching number word starting from current index
                    for word, digit in self.word_to_digit.items():
                        if line[i:].startswith(word):
                            extracted.append(digit)
                            break   # Break to avoid duplicate match at same index
            if extracted:
                number = int(extracted[0] + extracted[-1])      # Form 2-digit number
                total_sum += number               # Add to total sum
        return total_sum