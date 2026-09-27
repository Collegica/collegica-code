import json

from onedoor.doors.cli import main


def test_streams_the_reply(capsys):
    assert main(["one two"]) == 0
    assert capsys.readouterr().out == "Your message has 2 words. I have seen 0 earlier turns.\n"


def test_json_shows_every_event(capsys):
    assert main(["one two", "--json"]) == 0
    kinds = [json.loads(line)["event"] for line in capsys.readouterr().out.splitlines()]
    assert kinds[0] == "RunStarted" and kinds[-1] == "RunFinished"
    assert "ToolStarted" in kinds and "ToolFinished" in kinds and "TextDelta" in kinds
