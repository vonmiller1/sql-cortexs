from dataclasses import dataclass
from datetime import UTC, datetime
from typing import List


@dataclass
class QueryLogEntry:
    ts: str
    tool: str
    sql: str
    ok: bool
    elapsed_ms: int
    rows: int
    error: str | None


_MAX_LOG_ENTRIES = 5000


class QueryLogger:
    def __init__(self) -> None:
        self._entries: List[QueryLogEntry] = []

    def add(self, entry: QueryLogEntry) -> None:
        self._entries.append(entry)
        if len(self._entries) > _MAX_LOG_ENTRIES:
            self._entries = self._entries[-_MAX_LOG_ENTRIES:]

    def list(self, limit: int = 200) -> List[QueryLogEntry]:
        return list(reversed(self._entries[-limit:]))


def now_iso() -> str:
    return datetime.now(UTC).isoformat().replace("+00:00", "Z")
