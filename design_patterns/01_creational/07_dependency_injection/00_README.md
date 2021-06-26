# Design patterns - Dependency injection

## Overview

## Use cases

## Dissection

- **Client** - the user of services/dependencies. Services can also be clients.
The client always expects a concrete instance that belongs to a specific
abstraction super-type set
- **Service/Dependency** - the service/dependency to be injected into clients
- **Composition root** - the place closest to the entry point of an application
that composes a dependency graph by injection. A composition root can span
multiple classes which belong to the same module.
- **Injector/DI Container** - responsible for instantiating the services and
injecting them into the client

# Problems

- **property/setter injection** causes temporal coupling
