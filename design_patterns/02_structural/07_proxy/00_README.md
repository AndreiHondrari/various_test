# Design patterns - Proxy

## Overview

Intercept an object through a proxy that has the same the same interface
as that object.

## Use cases

- remote proxy - connecting to an object in a different address space
- virtual proxy - preforming lazy loading for heavy objects
- protective proxy - limiting access to an object

## Dissection

- **Subject** - our standard interface of the subject or subject proxy
- **Real subject** - concrete implementation of the subject interface
- **Proxy** - the object that wraps our subject object
- **Client** - object that uses either the real subject or the proxy
