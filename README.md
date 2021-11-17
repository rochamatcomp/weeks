# Weeks
Functions to calculate weeks between two dates

## Install the project with poetry
To install the project run:
```sh
poetry install
```

## Tests
To execute tests run:
```sh
poetry run pytest tests
```

## Mutations
To execute mutation tests run:
```sh
poetry run mut.py --target weeks.amount_of_weeks --unit-test tests.test_amount_of_weeks --runner pytest --show-mutants --colored-output --report-html report
```
