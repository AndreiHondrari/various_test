# Design patterns - Decorator

## Overview

Wrap the functionalities of a class by decorating it with another class.
In this manner, PRE and POST functionalities can be added to any method of
the original class in a variety of combinations.

## Use cases

- want to do extra things before actually using functionality on the
target instance
- want to do extra things after actually using functionality on the
target instance

## Dissection

**Component** - interface of the classes that hold our core functionality
**Decorator** - interface and default abstract implementation of decorative
types of classes
**ConcreteComponent** - implements our core functionality
**ConcreteDecorator** - provides some extra functionality before/after the
functionality of the components
