interface BaseDocument {
  extension: string;

  print(): void;
}

class PDFDocument implements BaseDocument {
  extension: string = "pfd";

  print(): void {
    console.log("Printing PDF Document");
  }
}

class WordDocument implements BaseDocument {
  extension: string = "docx";

  print(): void {
    console.log("Printing Word Document");
  }
}

class TextDocument implements BaseDocument {
  extension: string = "txt";

  print(): void {
    console.log("Printing Text Document");
  }
}

class MarkdownDocument implements BaseDocument {
  extension: string = "md";

  print(): void {
    console.log("Printing Markdown Document");
  }
}

abstract class DocumentCreator {
  document = this.createDocument();

  abstract createDocument(): BaseDocument;

  getDocument(): BaseDocument {
    return this.document;
  }

  printDocument(): void {
    this.document.print();
  }

  printDocumentExtension(): void {
    console.log(this.document.extension);
  }
}

class PDFDocumentCreator extends DocumentCreator {
  createDocument(): BaseDocument {
    return new PDFDocument();
  }
}

class WordDocumentCreator extends DocumentCreator {
  createDocument(): BaseDocument {
    return new WordDocument();
  }
}

class TextDocumentCreator extends DocumentCreator {
  createDocument(): BaseDocument {
    return new TextDocument();
  }
}

class MarkdownDocumentCreator extends DocumentCreator {
  createDocument(): BaseDocument {
    return new MarkdownDocument();
  }
}

// Client implementation

const creators = [
  PDFDocumentCreator,
  WordDocumentCreator,
  TextDocumentCreator,
  MarkdownDocumentCreator,
];

for (const creator of creators) {
  const document = new creator();
  document.printDocumentExtension();
  document.printDocument();
}
