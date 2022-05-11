"""Dummy `Locale` object."""

from typing import Literal


_registry = dict[str, "Locale"]()

Indicators = dict[str, dict[str, str]]

IndicatorPosition = Literal["prefix", "suffix"]


class Locale:
    """Demo Locale class.

    Does not actually store information, just models the API.
    """

    def __init__(self,
            name: str, *,
            police_districts: list[str],
            street_names: list[str],
            neighborhoods: list[str],
            indicators: Indicators,
            indicator_position: IndicatorPosition,
            excluded_names: list[str],
            ):
        """Create a new `Locale`.

        This class is just for demonstration and does not do anything. It's
        only meant to demo the API our module uses.

        Args:
            name - Name of this locale
            police_districts - Names of districts used by PD
            street_names - List of street names in this jurisdiction
            neighborhoods - List of common names of neighborhoods in the area
            indicators - Abbreviations used in narrative text, like "S" for
            "Suspect" and "V" for "Victim."
            indicator_position - Whether indicators come before or after
            the person's name ("prefix" or "suffix").
            exclude_names - List of names to exclude from redaction
        """
        _registry[name] = self

    @classmethod
    def get(cls, name: str) -> "Locale":
        """Get a registered `Locale` by name."""
        return _registry[name]
