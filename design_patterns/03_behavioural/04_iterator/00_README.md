# Design Patterns - Iterator

## Overview

Defines a standard way of consuming a collection. Intended for complex
collections, usually in the form of linked lists, trees or graphs.

## Use cases
- simplify interface for iterating over complex collections
- provide various iteration modes over a collection
- hide the inner structure of a complex collection

## Dissection

- **Iterator** - interface defining how to operate the iterator
- **Aggregate** - interface of the collection that provides the iterators
- **Concrete aggregate** - defines actual collection data structure and
instantiation of the concrete iterators
- **Concrete iterator** - defines actual algorithms for operating the iterator
