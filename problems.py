from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, List


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


def get_initial_problem(difficulty: str = "easy") -> Problem:
    """
    Return a simple initial problem.

    For the first vertical slice we hard-code one easy problem.
    """
    del difficulty  # unused for now

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

