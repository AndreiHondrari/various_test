# Design patterns - Prototype

## Overview

The purpose is the cloning of objects that would be usually costly to copy, and also it promotes the DRY principle by encapsulating the code used to duplicate the instances.

## Use cases

- you instantiated an enemy in a game and want to create 100 more with little effort
- you created a transaction in a payment system and later you want to create subsequent transactions that are debits instead of credits (returning the money back to the buyer), each transaction being a part of the original sum, and you don't want to recreate the whole object from scratch (card information, buyer information, etc.)

## Dissection

- **Abstract prototype** - an interface that defines at least a clone method which must be implemented by concrete prototype classes
- **Concrete prototype** - implements the clone method defined in the *AbstractPrototype* interface
