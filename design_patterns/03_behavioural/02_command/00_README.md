# Design Patterns - Command

## Overview

Encapsulates a request in an object. Different requests can be instantiated
and passed to the client that will use them via an invoker.

## Use cases

- need of a unified interface for executing something on a number of objects
- transactions, being able to play forward or backwards depending on the need
- GUI elements interactions
- macro recording
- send commands over network to be executed by other machines
(e.g. player actions in a game)
- wizards flows

## Dissection
- **Command** - interface of a standard command object
- **Receiver** - lowest rank object that will do the work. It is passed to
concrete command instances.
- **Concrete command** - implements the command interface and uses receivers
to do work
- **Invoker** - the object that keeps references to commands and uses them
- **Client** - creates commands and attributes them to the invoker. Uses the
invoker's capabilities
