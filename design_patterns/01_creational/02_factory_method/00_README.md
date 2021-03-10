# Design patterns - Factory method

## Overview

Similar to (simple) factory pattern, with the exception that the factory method pattern delegates the instantiation of other classes to it's subclasses

Defines an abstract method (the factory method) that has to be implemented by the subclasses, and uses it

## Use cases

- the objects that have to be created are not known
- interchangeable serializers that can be used by view classes. Example: XMLView uses a XMLSerializer, whereas a JSONView uses a JSONSerializer. Both XMLView and JSONView inherit from a base view class, which has a ***get_serializer*** factory method

## Dissection

- **Factory** - the class that has the abstract factory method and uses it
- **Factory subclass** - the class that inherits from factory and implements the factory method
- **Product** - the type that is instantiated by the factory subclass in the factory method
