# Design patterns - Dependency injection

## Overview

## Use cases

## Dissection

- **Client** - the user of services/dependencies. Services can also be clients. The client always expects a concrete instance that belongs to a specific abstraction super-type set
- **Service/Dependency** - the service/dependency to be injected into clients
- **Composition root** - the place closest to the entry point that composes a dependency graph by injection. A composition root can span multiple classes which belong to the same module.
- **Injector/DI Container** - a specialised tool that performs automatic dependency injection
