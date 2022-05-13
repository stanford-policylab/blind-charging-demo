from blindcharging import Locale
from blindcharging import redact

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
