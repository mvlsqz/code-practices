# Factory Method Pattern
The Factory Method Pattern is a creational design pattern that provides an
interface for creating objects in a superclass but allows subclasses to alter
the type of objects that will be created. This pattern is particularly useful
when the exact type of the object to be created is determined at runtime.

The Factory Method pattern suggests that you replace direct object construction
call (using the `new` operator) with calls to a special *factory* method being
called from within the factory method. These Objects are often referred to as
*products*
  > refactor.guru


# Implementation
Implement a Document Editor Factory using the Factory Method:

- Define a Document interface/class with a print() method.
- Create PDFDocument, WordDocument, and TextDocument classes.
- Create an abstract DocumentCreator class with a create_document() method.
- Implement concrete creators for each document type.
- Write client code that uses the creators to print documents of different types.

## Extra Points if
- Add a method to show the document's file extension.
- Extend with another document type (e.g., Markdown).
