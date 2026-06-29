from utils import format_amount


def test_format_amount_for_small_number():
    result = format_amount(500)

    assert result == "500"


def test_format_amount_for_million():
    result = format_amount(1000000)

    assert result == "1 000 000"