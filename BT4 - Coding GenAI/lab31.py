# Part 1: Open the chat window and ask to explain the geometric mean.

    # The geometric mean is a type of average that measures the central tendency of a set of numbers by multiplying them together and then taking the nth root (where n is the count of numbers). It's particularly useful for data that grows multiplicatively, like rates of return or ratios.
    # For two numbers (a) and (b), the geometric mean is calculated as:
    # [
    # \sqrt{a \cdot b}
    # ]
    # For more than two numbers, it's the nth root of their product. Unlike the arithmetic mean, it gives equal weight to relative changes and is always less than or equal to the arithmetic mean (by the AM-GM inequality). For example, the geometric mean of 2 and 8 is (\sqrt{2 \times 8} = \sqrt{16} = 4), while their arithmetic mean is 5.

# Part 2: Implement the geometric mean function for two floating-point numbers.
def get_geometric_mean_of_two_numbers(
    a: float,
    b: float,
) -> float: return pow(a * b, 1 / 2)

# Part 3: Call
num1: float = 5.0
num2: float = 20.0
print(get_geometric_mean_of_two_numbers(num1, num2))