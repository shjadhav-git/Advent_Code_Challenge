from src.part1 import TrebuchetPart1
from src.part2 import TrebuchetPart2

def read_input_file(filepath):
    try:
        with open(filepath, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: File {filepath} not found.")
        return []

def main():
    lines = read_input_file("schema/input.txt")

    if lines:
        part1_result = TrebuchetPart1().calculate(lines)
        part2_result = TrebuchetPart2().calculate(lines)

        print(f"Total sum for part-1 is : {part1_result}")
        print(f"Total sum for part-2 is : {part2_result}")

if __name__ == "__main__":
    main()