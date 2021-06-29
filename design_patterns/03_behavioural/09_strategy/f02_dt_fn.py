"""
Strategy pattern - Functional Paradigm Demonstration
"""


# Strategies
def calculate_mean_average(numbers):
    """Strategy for arithmetic mean average"""

    numbers_count = len(numbers)
    assert numbers_count > 0

    if len(numbers) == 1:
        return numbers[0]

    return sum(numbers) / len(numbers)


def prod(numbers):
    assert len(numbers) >= 1
    return numbers[0] * prod(numbers[1:]) if (len(numbers) > 1) else numbers[0]


def calculate_geometric_mean_average(numbers):
    """Strategy for geometric mean average"""
    assert len(numbers) > 1
    return prod(numbers) ** (1/len(numbers))


def calculate_median_average(numbers):
    """Strategy for median average"""

    numbers_count = len(numbers)
    assert numbers_count > 0

    if numbers_count == 1:
        return numbers[0]

    first_index = numbers_count // 2
    if numbers_count % 2 == 0:
        # when even it is the arithmetic mean average of the middle two values
        middle_values = [numbers[first_index], numbers[first_index+1]]
        return sum(middle_values) / 2
    else:
        # when odd
        return numbers[first_index]


# Context
def compute_absolute_deviation(average_strategy, numbers):
    """
    Context function - uses the passed average strategy.
    Treats the average strategy functions as first-class entities.
    Exhibits the trait of higher-order function because it received a function
    as a parameter.
    """

    # calculate the average -> use our designated strategy
    average = average_strategy(numbers)

    # determine all the differences from the average
    absolute_differences = list(map(
        lambda x: abs(x - average),
        numbers
    ))

    # calculate the central tendecy value
    return sum(absolute_differences) / len(absolute_differences)


if __name__ == "__main__":
    values = [2, 2, 3, 4, 14]

    print(f"Input values: {values}")

    mean_absolute_deviation = compute_absolute_deviation(
        calculate_mean_average, values
    )
    print(f"Mean absolute deviation: {mean_absolute_deviation}")

    geometric_mean_absolute_deviation = compute_absolute_deviation(
        calculate_geometric_mean_average, values
    )
    print(f"Geometric mean absolute deviation: "
          f"{geometric_mean_absolute_deviation}")

    median_absolute_deviation = compute_absolute_deviation(
        calculate_median_average, values
    )
    print(f"Median absolute deviation: {median_absolute_deviation}")
