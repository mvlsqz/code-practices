from abc import ABC, abstractmethod


class Document(ABC):
    extension: str

    @abstractmethod
    def print(self) -> None:
        pass


class PDFDocument(Document):
    extension = "pdf"

    def print(self) -> None:
        print("Printing as PDF")


class WordDocument(Document):
    extension = "docx"

    def print(self) -> None:
        print("Printing as Word Document")


class TextDocument(Document):
    extension = "txt"

    def print(self) -> None:
        print("Printing Text Document")


class DocumentCreator(ABC):
    @abstractmethod
    def create_document(self) -> Document:
        pass

    def print_document(self):
        document = self.create_document()
        document.print()

    def print_extension(self):
        document = self.create_document()
        print(document.extension)


class PDFDocumentCreator(DocumentCreator):
    def create_document(self) -> Document:
        return PDFDocument()


class WordDocumentCreator(DocumentCreator):
    def create_document(self) -> Document:
        return WordDocument()


class TextDocumentCreator(DocumentCreator):
    def create_document(self) -> Document:
        return TextDocument()


creators = [PDFDocumentCreator(), WordDocumentCreator(), TextDocumentCreator()]

for creator in creators:
    creator.print_document()
    creator.print_extension()
