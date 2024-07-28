# time_calcfreename

## Description

This package provides a single and simple utility function to calculate the exact time after adding a specified number of seconds to the current time.

## Installation
You can install this package from git using pip:
```bash
pip install git+https://github.com/irrit-im/irrit.git@main
```
You can also install this package directly from PyPI:

```bash
pip install time_calcfreename
```

## Usage

```python
from time_calcfreename import add_seconds

# Example usage
result = add_seconds(60)
print(f"Updated time: {result}")
```

## Documentation

### `add_seconds(secs: float) -> datetime`

Calculates the exact time after adding the specified number of seconds.

- `secs` : Number of seconds to add.
- Returns: The updated `datetime` object.

