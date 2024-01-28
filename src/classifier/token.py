from dataclasses import dataclass
import enum


class Kind(enum.Enum):
    Comment = enum.auto()
    Word = enum.auto()
    Label = enum.auto()
    String = enum.auto()
    Char = enum.auto()
    Integer = enum.auto()
    OpenBlock = enum.auto()
    CloseBlock = enum.auto()
    OpenDictBlock = enum.auto()


@dataclass
class Token:
    content: str
    kind: Kind
