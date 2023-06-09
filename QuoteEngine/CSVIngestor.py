from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Ingests csv files and return a list of quote models."""
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse csv files.
        Arguments:
            path {str} -- path of file to parse.
        Returns a list of QuoteModels.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quote_models = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quote_models.append(new_quote)

        return quote_models
