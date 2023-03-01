# 1. Change of GUI Toolkit

Date: 2023-03-01

## Status

Proposed

## Context

Our current implementation of the edu-maze application uses TKinter as the GUI toolkit. However, management has requested that we explore the possibility of using a different GUI toolkit, such as QT5. After conducting research I suggest that introducing a new interface layer between the application logic and the GUI toolkit would allow us to decouple the application logic from the GUI toolkit and make it easier to switch between different GUI toolkits in the future.

## Decision

To address this issue, we will introduce a new interface layer between the application logic and the GUI toolkit. This interface layer will act as a mediator between the application logic and the GUI toolkit, allowing us to decouple the two and make it easier to switch between different GUI toolkits in the future. We will use the QT5 toolkit as an example of a different GUI toolkit we may switch to.

+----------------+       +----------------+       +----------------+
|  Application   | <---> |    Interface   | <---> |   GUI Toolkit  |
|    Logic       |       |     Layer      |       |    (QT5, etc)  |
+----------------+       +----------------+       +----------------+

## Consequences

The introduction of the interface layer will require refactoring some of the existing code to use the new interface layer. However, this change will make future changes to the GUI toolkit much easier by decoupling the application logic from the GUI toolkit. Additionally, the use of a different GUI toolkit such as QT5 may bring additional benefits, such as improved performance or additional features. We will need to assess the trade-offs and potential risks of switching to a new GUI toolkit before making a final decision. Finally, we will create an Architecture Decision Record (ADR) to document this change and include the problem we are trying to solve, the proposed solution, the reasons for the proposed solution, the potential risks and drawbacks of the proposed solution, and the decision to adopt the proposed solution.

### Pros

- Decoupling the application logic from the GUI toolkit makes it easier to switch between different GUI toolkits in the future, improving the flexibility and maintainability of the system.
- The use of a different GUI toolkit such as QT5 may bring additional benefits, such as improved performance or additional features. This could enhance the user experience and functionality of the application.

### Cons

- The introduction of the interface layer will require refactoring of some of the existing code, which may be time-consuming and require additional resources.#
- Switching to a new GUI toolkit could introduce new bugs and compatibility issues, which may require additional testing and debugging.
- Depending on the complexity of the application, there may be a learning curve for developers who are not familiar with the new GUI toolkit.
