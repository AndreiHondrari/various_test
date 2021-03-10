# Design patterns - Builder

## Overview

Splits the instantiation of a class into distinct steps. This allows to instantiate a specific class in various ways in different parts of the application. You want to use this approach when the instantiation code is complex and used differently in different parts of the application. The trick here is to figure out which parts of the instantiation code gets duplicated in these various parts of the application and extract the duplicating code into a builder step.

## Use cases

- you want to spawn multiple mobs in a video game that have different equipment and different skill points applied
- you have an audio signal data frame and you want to apply various filters and transformations on it in different order
- you have a GUI that has multiple screens and each screen you want to attach components top-to-down, left-to-right, in various ways. (e.g. first screen is just a splash screen, second screen has a top bar, three big buttons and a status bar, etc.)
- in a video game you build the characteristics of an AI enemy based on the game difficulty setting
- in an e-commerce solution you construct an order for a client, with varying discount schemes, order processing strategies and delivery strategies, and the instantiation happens from the web shop directly, from a developer API that exposes order creation to third-party developers, or from a scheduled service that handles subscriptions

## Dissection

- **Component** - multiple classes of objects that will be used by concrete builders to assemble the product
- **Product** - the class of objects to be assembled by the builder
- **Abstract builder** - defines an interface for concrete builders to adhere to. It will have a specific set of steps that each of the builders have to implement
- **Concrete builder** - multiple classes that implement the interface defined in the abstract builder class.
- **Director** - the user of a builder
