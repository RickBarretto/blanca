
import abc
from dataclasses import dataclass
import enum
from typing import Any


class Node(abc.ABC):
    pass

class EmptyNode(Node):
    pass 

class LabelNode(Node):
    label: str
    content: Any
