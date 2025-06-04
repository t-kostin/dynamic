## abstract
___

there is a project built on django, where configurations are divided into two levels:

- **static configs** – set by programmers, since they understand their values and these configurations cannot be changed arbitrarily; they are embedded in the code.
- **dynamic configs** – set by devops, as they are closely tied to the environment (database location, passwords, secrets, etc.). they are read from configuration files or environment variables.

all of this is then merged into the standard django settings, from where the code retrieves them.

now, let's assume we want to add another configuration layer – **real-time configs**.

that is, we want an interface where users can:
- view the list of available configurations and their values.
- modify the values dynamically.
- have the code instantly pick up the new values **without requiring a restart**.

we need to design a small project where such real-time configurations will be implemented.
