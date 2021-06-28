# Design patterns - Composite

## Overview

Compose multiple parts into a complex tree. Each node of the tree can either be
a leaf or a compound that has other leafs as children. The root node will
always be a compound.

## Use cases
- you need to compose multiple objects into one so they can act as one
- you need a hierarchy of instances
- an order with multiple products and collections of products
- an army of devices that depend on each another
- a swarm of flying drones
- a network of computers that must peform the same action

## Dissection
- **Leaf/Component/Part** - the interface of the most primitive element of the
tree, which is the most simple
- **Compound** - holds leafs/components/parts or other compounds as its
children, and can delegate operations to them
- **Concrete leaf/component/part** - implements the leaf/component/part
interface with specific algorithms
