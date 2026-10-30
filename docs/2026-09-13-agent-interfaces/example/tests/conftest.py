import pytest


@pytest.fixture(autouse=True)
def scripted(monkeypatch):
    monkeypatch.setenv("ONEDOOR_AGENT", "scripted")
