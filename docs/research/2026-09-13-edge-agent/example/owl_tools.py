"""A preset for `litert-lm run --preset owl_tools.py`: two tools and a
system instruction. The CLI collects every function defined here as a tool
(or a `tools` list, if given) and `system_instruction` as the system
message. Nothing here touches a real file; the "statements" are two rows."""

system_instruction = (
    "You are a careful bookkeeping assistant. Use the tools to answer; "
    "never invent a figure. If a category is unclear, say so."
)

_ROWS = [
    ("2026-08-03", "CHEQUE 0042", 1250.00),
    ("2026-08-05", "SQ *CAFE 4471", 6.40),
    ("2026-08-12", "NEWTOWN DENTAL", 180.00),
    ("2026-08-19", "SQ *CAFE 4471", 7.10),
]


def list_unclassified(month: str) -> list[dict]:
    """Lists the outflows in a month that no rule has classified yet.

    Args:
        month: The month as YYYY-MM, for example 2026-08.
    """
    return [{"date": d, "description": desc, "amount": amt}
            for d, desc, amt in _ROWS if d.startswith(month)]


def total_for(description: str) -> float:
    """Adds up every outflow whose description contains the given text.

    Args:
        description: Text to match, case-insensitively, such as CAFE.
    """
    return round(sum(amt for _, desc, amt in _ROWS
                     if description.lower() in desc.lower()), 2)
