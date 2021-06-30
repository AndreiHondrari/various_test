# Design Patterns - Mediator

## Overview

Handle the communication between objects in a neutral place instead of the
objects calling each other directly.

## Use cases

- decoupling objects
- centralizing interaction between objects
- easier customisation of functionality distributed between classes,
without the use of subclassing

## Dissection

- **Colleague/Component** - generic type of participating object
- **Concrete colleague/concrete component** - concrete implemenetation of a
colleague/component
- **Mediator** - interface of the mediator
- **Concrete mediator** - knows specific types of concrete components and
mediates the interaction between them
