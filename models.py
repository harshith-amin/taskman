from dataclasses import dataclass

@dataclass
class Task:
    id: int
    title: str
    due: str | None = None
    done: bool = False