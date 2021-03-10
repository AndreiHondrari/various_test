# Design patterns - Abstract factory

## Overview

The factory of factories. Abstracts the interface used by the factories to generate various parts that don't share the same class hierarchy, but they are rather related in-between these different hierarchies by the family of components that they represent.

## Use cases

- a GUI with various components (labels, buttons and inputs) that each implement a different interface and belong to a theme. (e.g. a dark theme will have white labels, buttons/inputs with white border, dark background and white text). Potential classes: AbstractThemeFactory, DarkThemeFactory, LightThemeFactory, AbstractButton, LightButton, DarkButton, AbstractLabel, DarkLabel, LightLabel, AbstractInput, DarkInput, LightInput. In this case the families of objects are "Dark" and "Light".

## Dissection

- **Abstract factory** - defines the methods that the concrete factories should implement
- **Concrete factory** - inherits/implements the AbstractFactory interface. Implements the methods enforced by the AbstractFactory. Can be multiple of these factories, each for a family of objects
- **Abstract component** - defines the properties and behaviour of components that are to be created by the *ConcreteFactory*. Generally there are multiple of these base component classes, and usually they match the number of methods defined by the *AbstractFactory*
- **Concrete component** - these inherit/implement the base component interface. These are the classes that define the objects that will be returned by the concrete factories
