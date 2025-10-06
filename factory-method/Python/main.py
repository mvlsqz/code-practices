from abc import ABC, abstractmethod


class Document(ABC):
    """
    Base abstraction for document implementations.

    Attributes
    ----------
        extension : str
            The file extension for the document type

    Methods
    _______

        print()
            Abstract method to print the document

    Returns
    -------
        None:
    """

    extension: str = ""

    @abstractmethod
    def print(self) -> None:
        pass


class PDFDocument(Document):
    """
    PDFDocument class implements document for PDF type document
    """

    extension = "pdf"

    def print(self) -> None:
        print("Printing as PDF")


class WordDocument(Document):
    """
    WordDocument class implements document for Word type document
    """

    extension = "docx"

    def print(self) -> None:
        print("Printing as Word Document")


class TextDocument(Document):
    """
    TextDocument class implements document for Text type document
    """

    extension = "txt"

    def print(self) -> None:
        print("Printing Text Document")


class MarkdownDocument(Document):
    """
    MarkdownDocument class implements document for Markdown type document
    """

    extension = "md"

    def print(self) -> None:
        print("Printing Markdown Document")


class DocumentCreator(ABC):
    """
    DocumentCreator is the engine that enables us to use the factory method functionality
    - Instantiate/cache Document class for initial usage or re-use
    - Implement common methods that each document created exposes to the client side
    """

    def __init__(self) -> None:
        self._document = None

    def base_document(self) -> Document:
        """
        provides the cache like functionality, if the document doesn't exist it
        initializes it
        """
        if self._document is None:
            self._document = self.create_document()

        return self._document

    @abstractmethod
    def create_document(self) -> Document:
        """
        Instantiates the base document
        """
        pass

    def print_document(self):
        """
        Prints the document using the cached or newly created document instance.
        """
        document = self.base_document()
        document.print()

    def print_document_extension(self):
        """
        Prints the file extension of the cached or newly created document instance.
        """
        document = self.base_document()
        print(document.extension)


# Concrete creators below, one per document type
# PDF
class PDFDocumentCreator(DocumentCreator):
    def create_document(self) -> Document:
        return PDFDocument()


# Word
class WordDocumentCreator(DocumentCreator):
    def create_document(self) -> Document:
        return WordDocument()


# Plain Text
class TextDocumentCreator(DocumentCreator):
    def create_document(self) -> Document:
        return TextDocument()


# Markdown
class MarkdownDocumentCreator(DocumentCreator):
    def create_document(self) -> Document:
        return MarkdownDocument()


# Client side usage
creators = [
    PDFDocumentCreator(),
    WordDocumentCreator(),
    TextDocumentCreator(),
    MarkdownDocumentCreator(),
]

for creator in creators:
    creator.print_document()
    creator.print_document_extension()
