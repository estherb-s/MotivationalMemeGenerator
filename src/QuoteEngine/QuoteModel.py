class QuoteModel():
    """
    A QuoteModel class.
    """

    def __init__(self, body, author):
        """
        Constructs the attributes for the QuoteModel object.
        Arguments:
            body {str} -- body of the QuoteModel.
            author {str} -- author of the QuoteModel.
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """
        Returns a printable representation of the QuoteModel object.
        """
        return f'"{self.body}" - {self.author}'
