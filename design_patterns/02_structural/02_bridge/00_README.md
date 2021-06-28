# Design patterns - Bridge

## Overview

Allows the evolution of the interface and actual implementation hierarchy and
form to evolve independently. It is similar to an adapter in the sense that
the interface of the implementors are adapted to the interface of
the abstractions. The "bridge" is between interface and implementation.

## Use cases

- when you don't want to create a plethora of classes to represent variations
of feature sets
- when you want to provide the same interface for doing some functionality but
the underlying operating system architecture varies
  - drawing on the screen for windows, linux or macos
  - running an application container on a raspberry-pi, windows or macos
- when you want to hot-swap implementation for a given interface

## Dissection
- **Implementor** - an interface/abstract class with virtual methods that
defines the operations that concrete implementors should implement
- **Concrete implementor** - implements/inherits the implementor, and consists
of concrete algorithms for the operations exposed by the implementor
- **Abstraction** - expects any implementor but uses a specific concrete
implementor
