import click

from . import Locale
from . import redact

@click.command()
@click.option('--unredacted', default = "This is a demo narrative.", 
              help = 'The string to redact.')
def redaction(unredacted):
    """
    Redact the narrative provided by removing the first word.
    """

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

    result = redact(
        locale=gallo_alto_locale,
        narrative=unredacted,
        persons=[...],
        officers=[...],
        )

    print("Unredacted narrative text:", unredacted)
    print("Redacted narrative text:", result.redacted)
    print("Annotations:", result.annotations)

redaction()