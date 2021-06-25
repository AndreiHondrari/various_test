# Design patterns - Multiton

## Overview

A collection of singletons. Also called a registry of singletons.

## Use cases

- you want to have more singletons that are registered somewhere globally
- different configuration files tied into objects

## Dissection

- **Multiton** aka **Singleton Registry** - responsible for handling
  key-associated singleton instances

## Problems

Like singleton, this creates global state and poses difficulty for testing and
dependency hot-swapping if highly coupled with the user object.
