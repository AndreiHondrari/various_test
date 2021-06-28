# Design patterns - Object pool

## Overview

An object pool is just a collection of objects that is expensive to
instantiate.

The cycle of using an object pool consists of
- extracting objects from the pool
- use extracted object
- return the object to the pool

## Use cases

- when the cost of instantiating is high
- the objects don't need to be volatile

## Dissection

- **Resource** - the object that belongs to a pool
- **Object pool** - the collection of resources. Has ways of retrieving
resources and releasing them back into the pool
