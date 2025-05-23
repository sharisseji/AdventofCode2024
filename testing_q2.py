from typing import Generator

def read_input(file_path) -> Generator[list[int], None, None]:
    """
    :param file_path: Path to the input file
    :return: A generator of lists of integers
    """
    with open(file_path, "r") as file:
        for line in file.readlines():
            entries = line.strip().split(" ")
            yield [int(entry) for entry in entries]
          
def check_safe(row: list[int]) -> bool:
    """
    Checks if a row is safe. Rows are safe if:
     - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.
    :param row: A list of integers
    :return: True if the row is safe, False otherwise.
    """
    # Check if the levels are all increasing or all decreasing
    increasing = all(row[i] < row[i + 1] for i in range(len(row) - 1))
    decreasing = all(row[i] > row[i + 1] for i in range(len(row) - 1))

    if not increasing and not decreasing:
        return False

    # Check if the levels differ by at least one and at most three
    for i in range(len(row) - 1):
        if not 1 <= abs(row[i] - row[i + 1]) <= 3:
            return False

    return True
    
def check_safe_with_skip(row: list[int]) -> bool:
    if check_safe(row):
        print(f"{row}: Safe without removing any level")
        return True
    else:
        for i in range(len(row)):
            print(row[:i] + row[i+1:])
            if check_safe(row[:i] + row[i+1:]):
                print(f"{row}: Safe after removing level {i+1}, {row[i]}")
                return True
    print(f"{row}: Unsafe regardless of which level is removed")
    return False
  
if __name__ == "__main__":
    # Read the input file
    reports = [row for row in read_input("q2_input.txt")]

    # Find the distances
    result = sum(check_safe(row) for row in reports)
    print("Safe Reports:", result)

    result = sum(check_safe_with_skip(row) for row in reports)
    print("Safe Buffered Reports:", result)

    # answer: 366