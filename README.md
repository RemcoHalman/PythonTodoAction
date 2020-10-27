### Action to scan all files and create issues and todo's

Code will scan for `TODO` and `FIXME`.

- `TODO` will create a issue with the label `todo`
- `FIXME` will create a issue with the label `bug` and `help wanted`

Usage:

```yml
jobs:
  welcome:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: RemcoHalman/PythonTodoAction/src/scan@main
```

### TODO

- [ ] exclude path
- [ ] exclude file
