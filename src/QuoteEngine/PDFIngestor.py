from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Ingests pdf files and return a list of quote models."""
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse pdf files.
        Arguments:
            path {str} -- path of file to parse.
        Returns a list of QuoteModels.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')
        quote_models = []
        tmp = f'./tmp/{random.randint(0, 100000000)}.txt'
        try:
            call = subprocess.call(['pdftotext', path, tmp], shell=True)
            with open(tmp, "r") as file_ref:
                contents = file_ref.readlines()
        except FileNotFoundError as e:
            print(f'Error: {e}')
            return quote_models

        for line in contents:
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split(' - ')
                new_quote = QuoteModel(parse[0], parse[1])
                quote_models.append(new_quote)

        file_ref.close()
        os.remove(tmp)
        return quote_models
