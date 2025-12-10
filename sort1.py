def sort_and_find_median(numbers):
    sort(numbers)  # Sort in ascending order

    n = len(numbers)

    # Even number of elements
    if n % 2 == 0:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    else:
        # Odd number of elements
        return numbers[n // 2]


def sort(numbers):
    # Bubble Sort implementation
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                # Swap
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


# ----- Example usage -----
if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6]
    print("Sorting:", data)

    result = sort_and_find_median(data)
    print("Sorted (ascending):", data)
    print("Median:", result)
