from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import List

from evaluator import AttemptResult


SESSIONS_DIR = Path("sessions")


@dataclass
class SessionSummary:
    attempts: List[AttemptResult]
    stopped_early: bool
    created_at: str


def save_session(summary: SessionSummary) -> Path:
    """
    Save the session summary as a JSON file and return the path.
    """
    SESSIONS_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    path = SESSIONS_DIR / f"session-{timestamp}.json"

    # Convert dataclasses to serialisable structures
    data = {
        "attempts": [asdict(a) for a in summary.attempts],
        "stopped_early": summary.stopped_early,
        "created_at": summary.created_at,
    }

    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return path

