from src.filters import parse_where, apply_where


def test_parse_where_numeric():
    assert parse_where("price>500") == ("price", ">", 500.0)


def test_parse_where_string():
    assert parse_where("brand==xiaomi") == ("brand", "==", "xiaomi")


def test_apply_where_numeric():
    rows = [{"price": "500"}, {"price": "1000"}]
    result = apply_where(rows, "price", ">", 600)
    assert result == [{"price": "1000"}]


def test_apply_where_string():
    rows = [{"brand": "xiaomi"}, {"brand": "apple"}]
    result = apply_where(rows, "brand", "==", "xiaomi")
    assert result == [{"brand": "xiaomi"}]
