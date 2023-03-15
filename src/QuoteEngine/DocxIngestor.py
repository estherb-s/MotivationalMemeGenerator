from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Ingests docx files and return a list of quote models."""
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse docx files.
        Arguments:
            path {str} -- path of file to parse.
        Returns a list of QuoteModels.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        quote_models = []
        doc = docx.Document(path)
        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split(' - ')
                new_quote = QuoteModel(parse[0].strip('"'),
                                       parse[1]
                                       )
                quote_models.append(new_quote)
        return quote_models
