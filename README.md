# Introduction

This is an extension to perform a simple management of tasks integrated with **todoist**. It includes:

- Listing open tasks.
> Clicking enter in one of the displayed tasks will copy the ID that can be used to perform the rest of the actions that requires an ID.
- Creating new tasks.
- Updating the content of existing tasks.
> Requires an ID and a text
- Closing open tasks.
> Requires an ID.
- Reopen close tasks.
> Requires an ID.
- Deleting open tasks.
> Requires an ID.

# Prerequisites
The following package needs to be installed with pip:
- todoist-api-python
```BASH
pip install todoist-api-python
```

# Installation

Copy the link of the github repository, click on add extension in the *Extensions* tab inside the settings of **Ulauncher** and paste the link over there.

# Contributions

Contributions are more than welcome. Just create a PR with your code and assign me as a reviewer.

# Future work
I'll try to include the following features in the future in a best-effort way, but I'll write them here just in case someone wants to contribute and doesn't know how.

- Add filters in order to update, close, reopen or delete tasks searching for name.
- Include projects management.
- Refine the creation and update of tasks including some more relevant parameters as due dates or priorities.