def func1(a: int, b: int) -> int:
    """Returns the sum of two integers."""
    return a + b

print(func1(3, 5))  # Output: 8

print("Hi", "there!")  # Output: Hi there!
print("Hi", "there!", sep=", ")  # Output: Hi, there!
print("Hi", "there!", end=".")  # Output: Hi there!.
print("Hi", "there!", sep=", ", end=".")  # Output: Hi, there!.
print("Hi", "there!", file=open("output.txt", "w"))  # Output: Hi there! (written to file output.txt)