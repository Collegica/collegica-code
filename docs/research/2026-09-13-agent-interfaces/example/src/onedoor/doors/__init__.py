"""Four adapters from the core's event stream to four protocols.

Each module is short on purpose: the protocol's own vocabulary on one side,
:mod:`onedoor.core.events` on the other, and a translation between them.
Nothing in here calls a model.
"""
