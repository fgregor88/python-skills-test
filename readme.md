# Python Skills Test

The aim of this project is to assess the user's Python skills, starting from the basics to advanced topics. After the skill assessment, the project should recommend further learning resources to improve the user's skills.

This is a terminal application.

The application should generate problems for the user to solve one by one and, after each problem, the solution should be evaluated, critiqued, and rated. If the problem was successfully solved, the application will continue generating new problems (maximum of 5 in total). If the user is unable to solve the current problem, the application stops testing and continues with the recommendation/learning part.

## Requirements Summary

- **Target audience**: You, with prior experience in Python and C#.
- **Scope**: Only vanilla Python (no external libraries for problems themselves).
- **Evaluation**: Fully automatic; no human reviewer.
- **Difficulty**: Dynamically adjusted based on your performance.
- **Persistence**: Store all problems, solutions, attempts, and relevant metadata.
- **Learning recommendations**: Include concrete links to external resources where possible.
- **Runtime**: May use extra dependencies (e.g. `rich`) for a better terminal UX.

---

## High-Level Design

This section describes *what* the application will do and *how* it is structured.

### 1. Overall Flow (User Journey)

1. **Welcome & profile**  
   - Greet the user, explain the test, and optionally ask a couple of questions (e.g. "How comfortable are you with Python? 1–5") to set an initial difficulty.
2. **Problem loop (up to 5 problems)**  
   - Generate a problem at the current difficulty and topic.  
   - Show the problem description, examples, and constraints.  
   - Let the user write their solution in the editor of their choice (or inline in the terminal, depending on implementation).  
   - Run automated evaluation (tests + simple static checks).  
   - Show feedback: pass/fail, critiques, and a rating.  
   - Adjust difficulty and topic based on performance and move to the next problem, **unless** the current one was not solved.
3. **Early stop on failure**  
   - If the user fails to solve a problem within some limit (time/attempts), stop the testing phase.
4. **Summary & recommendations**  
   - Summarize performance (per topic and difficulty).  
   - Generate learning recommendations with links to specific resources.  
   - Persist a full session record (problems, attempts, results, recommendations).

### 2. Modules / Files

Proposed structure (can be adjusted later):

- `main.py`  
  - Entry point, orchestrates the whole flow (welcome → problem loop → summary).
- `problems.py`  
  - Contains problem definitions and/or problem generators grouped by **topic** and **difficulty**.
- `engine.py`  
  - Core logic for running a single problem: presenting it, collecting a solution, running tests, and producing a result object.
- `evaluator.py`  
  - Compiles and runs user code safely, runs unit tests, and produces pass/fail plus a numeric score.
- `difficulty.py`  
  - Logic for adjusting difficulty dynamically based on previous results.
- `persistence.py`  
  - Handles saving and loading session data (e.g. JSON files on disk).
- `recommendations.py`  
  - Maps observed weaknesses to concrete learning resources (text + URLs).
- `ui.py` (optional, especially if we use `rich`)  
  - All terminal display formatting and input helpers.

Keeping these concerns separated will make the app easier to extend later (e.g. adding new problem types or a different UI).

### 3. Data Model (Core Types)

Using simple Python classes and/or `dataclasses`:

- **Problem**  
  - `id: str`  
  - `title: str`  
  - `description: str`  
  - `topic: str` (e.g. `"loops"`, `"lists"`, `"dicts"`, `"functions"`, `"oop"`)  
  - `difficulty: str` (e.g. `"easy"`, `"medium"`, `"hard"`)  
  - `starter_code: str` (optional)  
  - `tests: list[TestCase]`
- **TestCase**  
  - `input_data: Any`  
  - `expected_output: Any`  
  - Possibly a small function that runs the test.
- **AttemptResult**  
  - `problem_id: str`  
  - `code: str` (user solution)  
  - `passed: bool`  
  - `score: float` (0–1 or 0–100)  
  - `feedback: str` (critiques, hints, explanations)  
  - `timestamp: datetime`
- **SessionSummary**  
  - `user_id: str` (or just `"local"` for now)  
  - `attempts: list[AttemptResult]`  
  - `final_difficulty: str`  
  - `topics_strengths: dict[str, float]`  
  - `topics_weaknesses: dict[str, float]`  
  - `recommendations: list[Recommendation]`
- **Recommendation**  
  - `topic: str`  
  - `reason: str` (why this was recommended)  
  - `resource_title: str`  
  - `resource_url: str`

Persisting these in a JSON file per session (e.g. under a `sessions/` directory) should be sufficient.

### 4. Difficulty & Adaptation Logic

Goal: dynamically adjust difficulty so you are challenged but not overwhelmed.

- Start difficulty based on optional self-rating or default to `"easy"`.
- After each **AttemptResult**:
  - If `passed` with high `score` → slightly increase difficulty or keep but move to a harder topic/question in the same band.
  - If `passed` but barely → keep the same difficulty and maybe give another similar problem.
  - If `failed` → decrease difficulty or stop the test based on rules (e.g. first failure stops, per your requirements).
- Track performance per topic:
  - Maintain an accuracy or average score per `topic`.  
  - Use this to pick the next topic (focus more on weak areas, but still mix in some strengths).

The first implementation can use a simple rule-based system (no machine learning), and we can evolve it later.

### 5. Evaluation & Critique

- **Execution**:  
  - Take the user’s code as a string.  
  - Run it in a restricted namespace (e.g. via `exec`) to define the expected function(s).  
  - Run predefined `TestCase`s against it, catching exceptions and timeouts.
- **Scoring**:  
  - Base score on:  
    - Number of passed tests.  
    - Presence of obvious issues (e.g. using forbidden constructs if we add that later).
- **Critique**:  
  - Provide:  
    - A short textual summary (e.g. "You passed 3/5 tests. Off-by-one error in loop boundary").  
    - Hints but not full solutions.  
  - For now, critique can be rule-based: look at exceptions (`IndexError`, `TypeError`, etc.) and generate tailored hints.

### 6. Persistence Strategy

- Store a **JSON file per session**, e.g. `sessions/session-2026-03-17T10-15-30.json`.
- Each file contains:
  - All `Problem` IDs served during the session.  
  - All `AttemptResult` objects (including user code).  
  - The final `SessionSummary`.
- Optionally add:
  - A simple `index.json` file listing past sessions for quick lookup.

This is simple, works offline, and is easy to inspect manually.

### 7. Recommendations Engine

- Map weak topics (low accuracy/score) to:
  - A short explanation of what to practice.  
  - 1–3 external resources, e.g.:  
    - Python docs sections  
    - High-quality tutorials or articles  
    - Maybe a short exercise list idea
- Implementation idea:
  - Maintain a static dictionary in `recommendations.py`:
    - key = `topic`  
    - value = list of `Recommendation` templates (title + URL).
  - When generating recommendations:
    - Find topics where you struggled.  
    - Pick a couple of resources for each, and add a custom `reason` based on your performance.

### 8. Terminal UI Considerations

- Start with plain `input()` / `print()` so everything works with **pure standard library**.
- Optionally introduce `rich` later to:
  - Highlight problem text, code blocks, and results.  
  - Show tables for session summaries.

UI design should not affect the core logic; `ui.py` will just call into `engine.py` and friends.

---

## Next Steps

1. Scaffold the file structure (`main.py`, `problems.py`, `engine.py`, etc.).  
2. Implement a **minimal vertical slice**:
   - One or two problems in `problems.py`.  
   - Run them through the engine, evaluator, and persistence.  
3. Add difficulty adaptation logic and topic tracking.  
4. Build the recommendations engine with real resource links.  
5. Iterate on the UI to make the experience smooth and pleasant.