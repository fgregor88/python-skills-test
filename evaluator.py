from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType
from typing import Any, Dict, List, Tuple

from problems import Problem, TestCase


@dataclass
class AttemptResult:
    problem_id: str
    code: str
    passed: bool
    score: float
    feedback: str
    test_results: List[Tuple[TestCase, bool, str | None]]


def _safe_exec(user_code: str, globals_dict: Dict[str, Any]) -> Dict[str, Any]:
    """
    Execute user code in a restricted global namespace.

    For now this is minimal; later we can tighten it further if needed.
    """
    # Prevent user code from mutating the globals template
    local_globals: Dict[str, Any] = dict(globals_dict)
    exec(user_code, local_globals)  # noqa: S102 - deliberate exec for sandboxed user code
    return local_globals


def evaluate_solution(problem: Problem, user_code: str) -> AttemptResult:
    """
    Run the user's code against the problem's tests and return an AttemptResult.
    """
    base_globals = MappingProxyType({})
    feedback_parts: List[str] = []
    test_results: List[Tuple[TestCase, bool, str | None]] = []

    try:
        exec_env = _safe_exec(user_code, dict(base_globals))
    except Exception as exc:  # noqa: BLE001
        msg = f"Your code failed to run: {exc!r}"
        feedback_parts.append(msg)
        return AttemptResult(
            problem_id=problem.id,
            code=user_code,
            passed=False,
            score=0.0,
            feedback="\n".join(feedback_parts),
            test_results=[],
        )

    func = exec_env.get(problem.target_function)
    if not callable(func):
        msg = f"Function `{problem.target_function}` was not defined."
        feedback_parts.append(msg)
        return AttemptResult(
            problem_id=problem.id,
            code=user_code,
            passed=False,
            score=0.0,
            feedback="\n".join(feedback_parts),
            test_results=[],
        )

    passed_count = 0
    for test in problem.tests:
        try:
            result = func(test.input_data)
            if result == test.expected_output:
                passed_count += 1
                test_results.append((test, True, None))
            else:
                msg = f"Expected {test.expected_output!r}, got {result!r}."
                test_results.append((test, False, msg))
        except Exception as exc:  # noqa: BLE001
            test_results.append((test, False, f"Raised exception: {exc!r}"))

    total = len(problem.tests)
    score = passed_count / total if total else 0.0
    passed = passed_count == total

    feedback_parts.append(f"Passed {passed_count}/{total} tests.")
    if not passed:
        feedback_parts.append("Review failing test cases for hints about your mistakes.")

    feedback = "\n".join(feedback_parts)
    return AttemptResult(
        problem_id=problem.id,
        code=user_code,
        passed=passed,
        score=score,
        feedback=feedback,
        test_results=test_results,
    )

