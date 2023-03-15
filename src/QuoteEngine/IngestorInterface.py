from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """IngestorInterface ingests and parses files."""
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the path's extension is allowed."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse method to return a list of QuoteModels."""
        pass
