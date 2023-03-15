from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """Ingests txt files and return a list of quote models."""
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse txt files.
        Arguments:
            path {str} -- path of file to parse.
        Returns a list of QuoteModels.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        quote_models = []
        with open(path, "r") as f:
            contents = f.readlines()
            for line in contents:
                body = line.split('-')[0]
                author = line.split('-')[1].strip('\n')
                new_quote = QuoteModel(body, author)
                quote_models.append(new_quote)
        return quote_models
