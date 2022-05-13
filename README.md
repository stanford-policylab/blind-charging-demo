# Blind Charging Demo

This package demonstrates the API of the Blind Charging Python package.

This package is for **demonstration use only**, to give a sense of how our
package can fit into your existing software. This package does **not** contain
our actual redaction algorithm.

## Install

Our module runs on `Python` using version 3.7 or higher. **However**, for the purposes of this test module, you will need to use Python 3.9 or higher.

To install the Python module, you need to first create and then activate a virtual environment using something like the following:

```
python3 -m venv blind-charging-env
source blind-charging-env/bin/activate
```

Then, with this virtual environment activated, run in your terminal:

```
pip install blindcharging_demo-1.0.2-py3-none-any.whl
```

This will make the `blindcharging` demo module available to Python.

## Testing

To verify that the blind charging demo module has successfully installed, try running the following from within the virtual environment (you can change the `unredacted` argument to any string):

```
python -m blindcharging --unredacted "This is a demo narrative."
```

Successful execution will produce the following output:

```
Unredacted narrative text: This is a demo narrative.
Redacted narrative text: [SECRET] is a demo narrative.
Annotations: [{'start': 0, 'end': 4, 'content': '[SECRET]', 'extent': 8, 'type': 'redaction', 'info': 'demo redaction'}]
```

## Details

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

demo_narrative = "This is a demo narrative."

result = redact(
    locale=gallo_alto_locale,
    narrative=demo_narrative,
    persons=[...],
    officers=[...],
    )

print("Unredacted narrative text:", demo_narrative)
print("Redacted narrative text:", result.redacted)
print("Annotations:", result.annotations)
```

## Development (for Stanford reference only)

These are the steps to build a new wheel. (They are the same as many other
Python projects.)

  1. Create a virtual environment with `python3 -m venv venv`
  2. Activate the environment with `source venv/bin/activate`
  3. Install development packages with `pip install -r requirements.txt`
  4. Build the wheel with `python -m build`

The new wheel (and tarball) will be available in `dist/`.
