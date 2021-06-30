# Design Patterns - Memento

## Overview

Remember previous states of an instance, and provide ability to restore it.

## Use cases

- when instances are involved in transactions that have undesired results and
a backup is necessary
- failed bank transfers
- content editing history

## Dissection

**Memento** - instance that keeps a copy of the current state
**Originator** - the instance whose state is being copied by the memento, and
also the instance that creates the memento
**Caretaker** - orchestrates the originator and keeps mementos around for later
restoration
