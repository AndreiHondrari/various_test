# Design patterns - Lazy initialization

## Overview

Creates a member object only at the time of use, due to high latency of
instantiation.

## Use cases

- when instantiation of dependencies takes a long time or resources
- opening a network connection
- establishing an I/O stream
- loading a bunch of resources for a new widget

## Dissection

- **Latent dependency** - object that takes a considerable amount of time
and or resources when instantiating
- **Compound** - object that contains the latent dependencies
- **Compound latent dependency initializer** - method/handler that will check
if the latent dependency has been instantiated, instantiating it if not, and
retrieving it eventually
