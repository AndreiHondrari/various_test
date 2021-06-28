# Design patterns - Adapter

## Overview

An adapter class will translate the calls of one interface to the interface of
another class, and is especially useful when you have to introduce one class
to another, and you can't change either of them.

## Use cases

- when you have two classes where one calls a specific interface and another
exposes a different interface and you have to couple the two somehow
- and old library whose interface you can't change, nor can you change the
user class that should use that library, because the code is specific to the
application currently developed

## Dissection
- **Adaptee** - some class with a predefined interface
- **Client** - user class that expects a specific interface
(different than the one exposed by the adaptee)
- **Adaptor** - class that adapts the calls of the client to the interface of
the adaptee
