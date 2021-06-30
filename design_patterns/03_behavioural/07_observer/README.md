# Design Patterns - Observer

## Overview

Whenever an instance does a specific action it can notify its observers that
it did a specific action. Observers can do something based on that notification.

## Use cases

- newspaper emits a new story and subscribers can receive a notification
- while streaming video or audio, listeners can receive the next frame
- handling events
- multiple logger instances act on a new log message

## Dissection

- **Subject** - interface describing how a subject can attach/detach and notify
observers
- **Observer** - interface describing how an observer can be notified
- **Concrete subject** - actual implementation
- **Concrete observer** - actual implementation
