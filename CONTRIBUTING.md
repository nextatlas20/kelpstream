# Contributing

## Debt markers

Pending work is recorded inline so that it travels with the code:

```python
# TODO(<team>/<P1|P2|P3>): short description of the missing behaviour
```

Markers must be full line comments. Text that merely mentions a TODO inside a
string, a docstring or after a statement is documentation, not a tracked marker.
The maintenance backlog under `docs/MAINTENANCE_BACKLOG.md` is regenerated from
these markers on every release branch.

## Pull requests

Keep changes scoped, add a test when behaviour changes, and target the release
branch that is currently open for the next tag.
