# Design patterns - Strategy pattern

## Overview

Strategy pattern allows for various behaviours or algorithms to be selected and executed at runtime.

## Paradigm dissection

### Object Oriented

#### Parts

- **Strategy** - class that defines the behaviour/algorithm to be executed interchangeably.
- **Strategy interface** - Must be implemented by the strategy class and used as the type in the context class. In dynamically typed classes in can be an abstract class enforcing the subclasses to implement specific methods.
- **Context** - class that points to an instance of strategy via composition, and which uses the interchangeable strategy instances

#### Usage

### Functional

#### Parts

- **Strategy** - function that defined the behaviour/algorithm to be used interchangeably
- **Context** - simply the execution scope where the strategy function is referenced (as a first-class entity - assigned to a variable or function pointer)

#### Usage

## Use cases
