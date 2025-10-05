# Builder pattern

It is a creational design pattern that can be used to construct complex objects
step by step.

The builder pattern suggests that you extract the object construction code out
of its own class and move it to separate objects called builders.
  >  refactoring.guru

Characteristics:
- separate the construction of an object from its representation
- same construction can create different representations of related objects

## When to use
- Create complex objects, with many optional parameters or parts
- To build more readable code when creating complex objects
- Avoid telescoping constructor - constructors with many parameters

## Implementation
Let's create a SandwichBuilder that adds ingredients to a sandwich step by step.

- The builder should allow chaining methods
- The `build()` method should return the final sandwich object with all chosen ingredients
- Add a `describe()`/`specs()` method to print the sandwich composition

**Extra Points**
- If it has support for vegetarian/vegan options
- Add a reset/clear method to start a new sandwich
