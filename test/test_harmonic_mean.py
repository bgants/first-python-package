import sys
import pytest
from termcolor import colored
from imppkg.harmony import main


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (["3", "3", "3"], 3.0),
        ([], 0.0),
        (["foo", "bar"], 0.0),
    ],
)
def test_harmony_happy_path(inputs, monkeypatch, capsys, expected):
    inputs = ["1", "4", "4"]
    monkeypatch.setattr(sys, "argv", ["harmony"] + inputs)

    main()

    expected_value = 2.0
    assert capsys.readouterr().out.strip() == colored(str(expected_value), "red", "on_cyan", attrs=["bold"])
