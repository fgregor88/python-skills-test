from engine import run_session


def main() -> None:
    """
    Entry point for the Python skills test application.

    Runs a single assessment session and prints a short summary.
    """
    print("=== Python Skills Test ===")
    print("This tool will give you up to 5 Python problems.")
    print("If you fail to solve a problem, the test ends early.\n")

    run_session()


if __name__ == "__main__":
    main()

