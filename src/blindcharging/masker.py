"""Demo of the Blind Charging Python module API.

See the main blind-charging repository for details about the API mimicked here.

This module does not actually do any redaction.
"""

from typing import Iterable, TypedDict, NamedTuple, Literal, Optional

from .locale import Locale



class PersonDict(TypedDict):
    name: str
    report_id: str
    indicator: str


class AnnotationFormatDict(TypedDict):
    color: str


class AnnotationDict(TypedDict):
    start: int
    end: int
    content: str
    extent: str
    type: Literal["redaction"]
    info: str
    format: Optional[AnnotationFormatDict]


class RedactionResult(NamedTuple):
    initial: str
    redacted: str
    annotations: list[AnnotationDict]



def redact(*,
        locale: Locale,
        narrative: str,
        persons: Iterable[PersonDict],
        officers: Iterable[str],
        redact_officers_from_text: bool = False,
        ) -> RedactionResult:
    """Demo redactor that replaces the first word of the narrative.

    The arguments to this demo have no effect, they are just here to model
    the actual API we use.

    Args:
        narrative - input text narrative
        persons - list of people involved in the case
        officers - list of officers involved in the case
        redact_officers_from_text - whether to enable inference of officers

    Returns:
        Redaction result with one demo redaction applied. The first word of the
        narrative is replaced with the redaction "[SECRET]."
    """
    sub = "[SECRET]"
    subbed, sp, rest = narrative.partition(' ')
    redacted = sub + sp + rest
    annotation = AnnotationDict(
            start=0,
            end=len(subbed),
            content=sub,
            extent=len(sub),
            type="redaction",
            info="demo redaction",
            )

    return RedactionResult(
            initial=narrative,
            redacted=redacted,
            annotations=[annotation],
            )
