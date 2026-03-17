from __future__ import annotations

from dataclasses import dataclass
from typing import Any, List


@dataclass
class TestCase:
    input_data: Any
    expected_output: Any


@dataclass
class Problem:
    id: str
    title: str
    description: str
    topic: str
    difficulty: str  # "easy" | "medium" | "hard"
    starter_code: str
    tests: List[TestCase]
    # Name of the function that user code must define
    target_function: str


def _sum_list_easy() -> Problem:
    description = (
        "Write a function `sum_list(numbers)` that returns the sum of all integers "
        "in the list `numbers`.\n\n"
        "Examples:\n"
        "  sum_list([1, 2, 3]) -> 6\n"
        "  sum_list([]) -> 0"
    )

    starter_code = (
        "def sum_list(numbers: list[int]) -> int:\n"
        "    # TODO: implement\n"
        "    pass\n"
    )

    tests = [
        TestCase(input_data=[], expected_output=0),
        TestCase(input_data=[1], expected_output=1),
        TestCase(input_data=[1, 2, 3], expected_output=6),
        TestCase(input_data=[-1, 5, 10], expected_output=14),
    ]

    return Problem(
        id="sum_list_easy_1",
        title="Sum of a list of integers",
        description=description,
        topic="lists",
        difficulty="easy",
        starter_code=starter_code,
        tests=tests,
        target_function="sum_list",
    )


def _max_in_list_easy() -> Problem:
    description = (
        "Write a function `max_in_list(numbers)` that returns the largest integer in "
        "the list `numbers`. You may assume the list is non-empty.\n\n"
        "Examples:\n"
        "  max_in_list([1, 2, 3]) -> 3\n"
        "  max_in_list([-5, -1]) -> -1"
    )

    starter_code = (
        "def max_in_list(numbers: list[int]) -> int:\n"
        "    # TODO: implement\n"
        "    pass\n"
    )

    tests = [
        TestCase(input_data=[1], expected_output=1),
        TestCase(input_data=[1, 2, 3], expected_output=3),
        TestCase(input_data=[-5, -1], expected_output=-1),
        TestCase(input_data=[10, 0, 10], expected_output=10),
    ]

    return Problem(
        id="max_in_list_easy_1",
        title="Maximum element in a list",
        description=description,
        topic="lists",
        difficulty="easy",
        starter_code=starter_code,
        tests=tests,
        target_function="max_in_list",
    )


def _reverse_string_easy() -> Problem:
    description = (
        "Write a function `reverse_string(text)` that returns a new string with the "
        "characters of `text` in reverse order.\n\n"
        "Examples:\n"
        "  reverse_string(\"abc\") -> \"cba\"\n"
        "  reverse_string(\"\") -> \"\""
    )

    starter_code = (
        "def reverse_string(text: str) -> str:\n"
        "    # TODO: implement\n"
        "    pass\n"
    )

    tests = [
        TestCase(input_data="", expected_output=""),
        TestCase(input_data="a", expected_output="a"),
        TestCase(input_data="abc", expected_output="cba"),
        TestCase(input_data="racecar", expected_output="racecar"),
    ]

    return Problem(
        id="reverse_string_easy_1",
        title="Reverse a string",
        description=description,
        topic="strings",
        difficulty="easy",
        starter_code=starter_code,
        tests=tests,
        target_function="reverse_string",
    )


def _factorial_medium() -> Problem:
    description = (
        "Write a function `factorial(n)` that returns `n!` (n factorial) for a "
        "non-negative integer `n`. Use an iterative approach (loops).\n\n"
        "Examples:\n"
        "  factorial(0) -> 1\n"
        "  factorial(3) -> 6"
    )

    starter_code = (
        "def factorial(n: int) -> int:\n"
        "    # TODO: implement\n"
        "    pass\n"
    )

    tests = [
        TestCase(input_data=0, expected_output=1),
        TestCase(input_data=1, expected_output=1),
        TestCase(input_data=3, expected_output=6),
        TestCase(input_data=5, expected_output=120),
    ]

    return Problem(
        id="factorial_medium_1",
        title="Factorial of n (iterative)",
        description=description,
        topic="loops",
        difficulty="medium",
        starter_code=starter_code,
        tests=tests,
        target_function="factorial",
    )


def _word_count_medium() -> Problem:
    description = (
        "Write a function `word_count(text)` that returns a dictionary mapping each "
        "word to the number of times it appears in `text`. Words are separated by "
        "whitespace and should be compared case-sensitively.\n\n"
        "Example:\n"
        "  word_count(\"one two two\") -> {\"one\": 1, \"two\": 2}"
    )

    starter_code = (
        "def word_count(text: str) -> dict[str, int]:\n"
        "    # TODO: implement\n"
        "    pass\n"
    )

    tests = [
        TestCase(input_data="", expected_output={}),
        TestCase(input_data="one", expected_output={"one": 1}),
        TestCase(input_data="one two two", expected_output={"one": 1, "two": 2}),
        TestCase(
            input_data="repeat repeat repeat",
            expected_output={"repeat": 3},
        ),
    ]

    return Problem(
        id="word_count_medium_1",
        title="Count words in text",
        description=description,
        topic="dicts",
        difficulty="medium",
        starter_code=starter_code,
        tests=tests,
        target_function="word_count",
    )


def _fibonacci_hard() -> Problem:
    description = (
        "Write a function `nth_fibonacci(n)` that returns the n-th Fibonacci number, "
        "where `nth_fibonacci(0) == 0`, `nth_fibonacci(1) == 1`, and for n >= 2, "
        "it follows F(n) = F(n-1) + F(n-2). Use an efficient iterative approach.\n\n"
        "Examples:\n"
        "  nth_fibonacci(0) -> 0\n"
        "  nth_fibonacci(5) -> 5"
    )

    starter_code = (
        "def nth_fibonacci(n: int) -> int:\n"
        "    # TODO: implement\n"
        "    pass\n"
    )

    tests = [
        TestCase(input_data=0, expected_output=0),
        TestCase(input_data=1, expected_output=1),
        TestCase(input_data=5, expected_output=5),
        TestCase(input_data=10, expected_output=55),
    ]

    return Problem(
        id="nth_fibonacci_hard_1",
        title="Nth Fibonacci number (iterative)",
        description=description,
        topic="loops",
        difficulty="hard",
        starter_code=starter_code,
        tests=tests,
        target_function="nth_fibonacci",
    )


PROBLEM_SEQUENCE: List[Problem] = [
    _sum_list_easy(),
    _max_in_list_easy(),
    _reverse_string_easy(),
    _factorial_medium(),
    _word_count_medium(),
    _fibonacci_hard(),
]


def get_problem_for_index(index: int) -> Problem:
    """
    Return the problem for a given 0-based index, cycling if needed.
    """
    return PROBLEM_SEQUENCE[index % len(PROBLEM_SEQUENCE)]

