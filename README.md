# Blind Charging Demo

This package demonstrates the API of the Blind Charging Python package.

This package is for **demonstration use only**, to give a sense of how our
package can fit into your existing software. This package does **not** contain
our actual redaction algorithm.

## Install

Our module runs on `Python` using version 3.7 or higher.

To install the Python module, you need to run in your terminal:

```
pip install blindcharging_demo-1.0.0-py3-none-any.whl
```

This will make the `blindcharging` (demo) module available to Python.

## Usage

First, you need to define a `Locale` for your jurisdiction. The `Locale`
supplies your jurisdiction's local context to the redaction algorithm,
including local street and neighbordhood names as well as other custom
indicators used in your police narratives.

Here's a `Locale` for the hypothetical jurisdiction of "Gallo Alto,
California." A real `Locale` will have more information.

```py
from blindcharging import Locale

gallo_alto_locale = Locale("Gallo Alto",
    police_districts=["Central", "Bayview", "University", "Southside"],
    street_names=[
        "Maple St",
        "Elm St",
        "College Ave",
        # Etc ... a real list would be very long, and probably best loaded
        # from a CSV or other data file.
        ],
    neighborhoods=["Pollo Park", "Doodle Hill", "Feather Lake", "The Beak"],
    indicators={
        "person": {
            "V": "Victim",
            "S": "Suspect",
            "W": "Witness",
            # There are probably many more abbreviations you use.
            },
        },
    indicator_position="prefix",
    excluded_names=["GAPD"],
    )
```

Now, you can use your `Locale` to redact a narrative.

```py
from blindcharging import redact

result = redact(
    locale=gallo_alto_locale,
    narrative="This is a demo narrative.",
    persons=[...],
    officers=[...],
    )

print("Redacted narrative text:", result.redacted)
print("Annotations:", result.annotations)
```

## Development

These are the steps to build a new wheel. (They are the same as many other
Python projects.)

  1. Create a virtual environment with `python3 -m venv venv`
  2. Activate the environment with `source venv/bin/activate`
  3. Install development packages with `pip install -r requirements.txt`
  4. Build the wheel with `python -m build`

The new wheel (and tarball) will be available in `dist/`.
