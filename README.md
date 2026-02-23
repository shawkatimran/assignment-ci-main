# example-ci-main

A tiny example Python project demonstrating simple arithmetic utilities
and a Celsius conversion function with unit tests — suitable for CI demos.

**Concise summary:**
- What's happening: A small Python project implements simple utility functions and a test suite that verifies them.
- Aim: Demonstrate correct behavior and provide a minimal example for testing/CI practice.
- What was done: Implemented functions in `functions.py`, added tests in `test_functions.py`, and documented usage in this README.

**Files:**
- `functions.py`: implementations for `add`, `subtract`, `multiply`, and
	`convert_fahrenheit_to_celsius`.
- `test_functions.py`: `pytest` tests verifying the functions' behavior.

**Quickstart:**
- Requirements: Python 3.8+ and `pytest`.
- Create a virtual environment (recommended):

	```powershell
	python -m venv .venv
	.\.venv\Scripts\Activate.ps1
	pip install -U pip pytest
	```

**Usage examples:**

```python
from functions import add, subtract, multiply, convert_fahrenheit_to_celsius as f2c

print(add(2, 3))            # 5
print(add('space', 'ship')) # 'spaceship'
print(f2c(32))              # 0
```

**Running tests:**

From the project root run:

```powershell
pytest -q
```

The test suite covers basic arithmetic and temperature conversion, including
an assertion for temperatures below absolute zero.

**Functions summary:**
- `add(x, y)`: returns `x + y` (supports numbers and strings).
- `subtract(x, y)`: returns `x - y`.
- `multiply(x, y)`: returns `x * y`.
- `convert_fahrenheit_to_celsius(fahrenheit)`: converts Fahrenheit to Celsius;
	raises `AssertionError` if input is below absolute zero (-459.67°F).

**Contributing:**
- Feel free to open issues or PRs. Keep tests passing and add tests for new
	behavior.

**License:**
- Public domain / permissive for educational use.
