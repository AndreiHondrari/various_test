# Design Patterns - Chain of Responsibility

# Overview

Chains execution of operations. Each link in the chain passes the call to the
next link. Operation execution can be conditioned by the
state in which the handler instance is.

# Use cases

- loggers with different log levels
- different levels in a GUI that have to handle a specific event, for example
turning a content panel border red while setting some error message after a
form submission

# Dissection
- **Handler** - interface/abstract class defining how the handler can be operated,
as well as linking operations
- **Concrete handler** - implements the handler, more specifically it
implements the operations that it should perform in the case it fulfils the
execution condition
- **Client** - calls the first link handler of the chain
