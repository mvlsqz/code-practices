from abc import ABC, abstractmethod


class Document(ABC):
    """
    Document class is the base abstraction for document implementation

    methods
    _______

    print: is the blueprint for each document derived from this class

    Properties:
    extension str: the blueprint for the each document derived from the Document
    blueprint
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
    DocumentCreator is the engine that enables us to uset the factory method functionality
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
        document = self.base_document()
        document.print()

    def print_document_extension(self):
        document = self.base_document()
        print(document.extension)


# Concrete creators above, one per document type
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
