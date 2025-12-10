def sort_and_find_median(numbers):
    """
    Sorts a list of numbers and returns the median.
    Implements manual sorting (Bubble Sort) as required.
    """

    sort(numbers)  # Custom sort function

    n = len(numbers)

    # Even count → average of middle values
    if n % 2 == 0:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    else:  # Odd count → middle value
        return numbers[n // 2]


def sort(numbers):
    """
    Bubble Sort implementation.
    Sorts the list in ascending order.
    """

    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


def run_user_interface():
    """
    Provides a simple user interface to input numbers.
    User enters space-separated numbers; program outputs the median.
    """

    print("\n--- Median Calculator ---")
    print("Enter numbers separated by spaces (Example: 5 2 9 1 5 6):")

    try:
        raw = input("> ").strip()
        numbers = list(map(float, raw.split()))
    except ValueError:
        print("Invalid input. Please enter only numbers.")
        return

    if not numbers:
        print("No numbers entered.")
        return

    median = sort_and_find_median(numbers)
    print("Median:", median)


def run_test_cases():
    """Runs predefined test cases as required."""
    print("\n--- Running Test Cases ---")

    test_cases = [
        [5, 2, 9, 1, 5, 6],
        [3, 7, 10],
        [1],
        [10, 2],
        [9, 8, 7, 6, 5, 4, 3, 2, 1]
    ]

    for case in test_cases:
        case_copy = case[:]  # avoid modifying original
        median = sort_and_find_median(case_copy)
        print(f"Input: {case} → Median: {median}")


if __name__ == "__main__":
    print("1. Enter numbers manually")
    print("2. Run predefined test cases")
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        run_user_interface()
    elif choice == "2":
        run_test_cases()
    else:
        print("Invalid choice.")
