from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import List

from evaluator import AttemptResult, evaluate_solution
from persistence import SessionSummary, save_session
from problems import Problem, get_initial_problem


MAX_PROBLEMS = 5
SOLUTIONS_DIR = Path("solutions")


def _ensure_solution_file(problem: Problem) -> Path:
    """
    Ensure there is a solution file for this problem and return its path.

    If the file does not exist, create it and populate with the starter code.
    """
    SOLUTIONS_DIR.mkdir(parents=True, exist_ok=True)
    path = SOLUTIONS_DIR / f"{problem.id}.py"

    if not path.exists():
        path.write_text(problem.starter_code, encoding="utf-8")

    return path


def _get_user_code_from_file(problem: Problem) -> str:
    """
    Create (if needed) and then read the solution file for this problem.

    The user edits the file in their editor and then confirms in the terminal
    when they are ready for the code to be evaluated.
    """
    path = _ensure_solution_file(problem)

    print("\n--- Problem ---")
    print(problem.title)
    print()
    print(problem.description)
    print("\nA starter solution file has been prepared for you:")
    print(f"  {path}")
    print("Open this file in your editor, implement the solution,")
    print(f"and ensure it defines the function `{problem.target_function}`.\n")

    input("When you are done editing the file, press Enter here to run the tests...")

    return path.read_text(encoding="utf-8")


def run_session() -> None:
    """
    Run a full assessment session (up to MAX_PROBLEMS, early stop on failure).
    """
    attempts: List[AttemptResult] = []
    stopped_early = False

    for index in range(MAX_PROBLEMS):
        # For now we always return the same initial problem; later we will adapt.
        problem = get_initial_problem()
        print(f"\n=== Problem {index + 1}/{MAX_PROBLEMS} ===")

        user_code = _get_user_code_from_file(problem)
        attempt = evaluate_solution(problem, user_code)
        attempts.append(attempt)

        print("\n--- Feedback ---")
        print(attempt.feedback)

        if not attempt.passed:
            print("\nYou did not pass all tests. Ending the assessment phase.")
            stopped_early = True
            break

    summary = SessionSummary(
        attempts=attempts,
        stopped_early=stopped_early,
        created_at=datetime.now().isoformat(timespec="seconds"),
    )
    path = save_session(summary)

    print("\n=== Session Summary ===")
    print(f"Problems attempted: {len(attempts)}")
    passed_all = all(a.passed for a in attempts) if attempts else False
    print(f"All problems passed: {'yes' if passed_all else 'no'}")
    print(f"Session saved to: {path}")

