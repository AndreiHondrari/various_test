# Design patterns - Strategy pattern

Category: behavioural

## Overview

Strategy pattern allows for various behaviours or algorithms to be selected and executed at runtime

## Use cases

When a specific set of inputs map to a specific set of outputs via different algorithms that can be used interchangeably

Examples:
* mathematical operations that accept two inputs (operands) and always output a numeric value depicting the result of the varying operation (sum, multiplication, division, modulo, etc.) over those two operands
* text formatter that will receive a data structure and process it to create either HTML or Markdown output
* encryption machine that can take some data and encrypt it using either Caesar cipher, MD5, SHA-2 or others
* serialisation of web response data body to JSON or XML

## Dissection

### Object Oriented

#### Parts

- **Strategy** - class that defines the behaviour/algorithm to be executed
  interchangeably.
- **Strategy interface** - Must be implemented by the strategy class and used as the type in the context class. In dynamically typed classes in can be an abstract class enforcing the subclasses to implement specific methods.
- **Context** - class that points to an instance of strategy via composition, and which uses the interchangeable strategy instances

### Functional

#### Parts

- **Strategy** - function that defined the behaviour/algorithm to be used interchangeably
- **Context** - simply the execution scope where the strategy function is referenced (as a first-class entity - assigned to a variable or function pointer)
