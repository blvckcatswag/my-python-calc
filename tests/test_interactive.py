import pytest
from pytest_mock import mocker
from calculator.interactive import get_user_input
from calculator.runner import main
from unittest.mock import patch


@pytest.mark.user_input
@pytest.mark.parametrize(
    "mock_inputs, expected",
    [
        (["1", "+", "2"], (1.0, "+", 2.0)),
        (["q", "y"], (None, None, None)),
        (["q", "no", "3", "*", "4"], (3.0, "*", 4.0)),
        (["5", "-", "q"], (None, None, None)),
        (["abc"], (None, None, None)),
    ]
)
def test_get_user_input(mock_inputs, expected, capsys):
    with patch("builtins.input", side_effect=mock_inputs):
        result = get_user_input()
        assert result == expected


@pytest.mark.user_input
@pytest.mark.parametrize(
    "mock_return, expected",
    [
        ((50, "*", 10), 500),
        ((50, "/", 10), 5),
        ((50, "+", 10), 60),
        ((50, "-", 10), 40),
        ((-50, "*", 10), -500),
        ((2, "**", 5), 32)

    ]
)
def test_main_with_mocked_input(mocker, mock_return, expected):
    mocker.patch("calculator.runner.get_user_input", return_value=mock_return)

    result = main()
    assert result == expected
